from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
import os
import shutil

app = FastAPI()

# --- Configuration & CORS ---
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://localhost:5174"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"]
)

# --- Pydantic Models ---
class VideoMetadata(BaseModel):
    id: str
    url: str
    title: str
    thumbnail: str
    author: str

class DownloadRequest(BaseModel):
    url: str
    is_audio: bool = False

class PlaylistRequest(BaseModel):
    url: str
    is_audio: bool = False

# --- Helper Functions ---
def cleanup_file(path: str):
    """Deletes a file or directory after the response is sent."""
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        print(f"Cleaned up: {path}")
    except Exception as e:
        print(f"Error cleaning up {path}: {e}")

def download_logic(url: str, is_audio: bool) -> str:
    """Synchronous download logic to be run in a threadpool."""
    yt = YouTube(url, on_progress_callback=on_progress)
    safe_title = "".join([c for c in yt.title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    
    if is_audio:
        stream = yt.streams.get_audio_only()
        filename = f"{safe_title}.m4a"
        download_path = stream.download(filename=filename)
    else:
        stream = yt.streams.get_highest_resolution()
        filename = f"{safe_title}.mp4"
        download_path = stream.download(filename=filename)
    
    return download_path

# --- Endpoints ---

@app.get('/', response_model=VideoMetadata)
async def get_video_metadata(url: str):
    try:
        print(f"Verifying video from {url}")
        # Run blocking pytube call in a separate thread
        yt = await run_in_threadpool(YouTube, url)
        
        return VideoMetadata(
            id=yt.video_id,
            url=url,
            title=yt.title,
            thumbnail=yt.thumbnail_url,
            author=yt.author
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching video: {str(e)}")

@app.post('/download')
async def download_video(request: DownloadRequest, background_tasks: BackgroundTasks):
    try:
        print(f"Downloading from {request.url}")
        # Run blocking download in a separate thread
        file_path = await run_in_threadpool(download_logic, request.url, request.is_audio)
        
        filename = os.path.basename(file_path)
        
        # Schedule file deletion after response is sent
        background_tasks.add_task(cleanup_file, file_path)
        
        return FileResponse(
            path=file_path, 
            filename=filename, 
            media_type='application/octet-stream'
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Download failed: {str(e)}")

def fetch_playlist_info(url: str):
    """Helper to fetch playlist info synchronously."""
    try:
        print(f"Initializing Playlist for {url}")
        pl = Playlist(url)
        
        # Force fetch of title to verify it works
        title = pl.title
        print(f"Playlist title: {title}")
        
        videos = []
        # Limit to 50 using manual counter to avoid IndexError on slicing
        count = 0
        for video in pl.videos:
            if count >= 50:
                break
            try:
                videos.append({
                    "title": video.title,
                    "url": video.watch_url,
                    "thumbnail": video.thumbnail_url,
                    "author": video.author
                })
                count += 1
            except Exception as e:
                print(f"Error processing video: {e}")
                continue
                
        return {
            "title": title,
            "total_videos": len(pl.videos),
            "preview_videos": videos,
            "msg": "Playlist loaded successfully"
        }
    except Exception as e:
        print(f"Error in fetch_playlist_info: {e}")
        import traceback
        traceback.print_exc()
        raise e

@app.get('/playlist')
async def get_playlist_metadata(url: str):
    try:
        print(f"Fetching playlist from {url}")
        # Run the entire heavy lifting in a separate thread
        data = await run_in_threadpool(fetch_playlist_info, url)
        return data
    except Exception as e:
        print(f"Endpoint error: {e}")
        raise HTTPException(status_code=400, detail=f"Error fetching playlist: {str(e)}")

