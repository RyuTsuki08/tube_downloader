from fastapi import FastAPI
from typing import Union
from pytube import YouTube, Playlist
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class Video:  
    def __init__(self, id: str, url : str, tile: str, thumbnail: str, author: str):
        self.id = id
        self.url = url
        self.tile = tile
        self.thumbnail = thumbnail
        self.author = author

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def get_video_by_url(url: str):
    try:
        print(f"Veryfing video from {url}")
        yt = YouTube(url)
        # yt.streams.filter(only_audio=True).first().download()
        vdo = Video(yt.video_id,  url, yt.title, yt.thumbnail_url, yt.author)
        return {'msg': 'Video loaded successfuly', 'video': vdo}
    except Exception as e:
        return { "msg": "Error Server", "error": e}
@app.post('/download')
def  download_video_or_audio(url: str, type: bool):
    try:
        print(f"Downloading from {url}")
        yt = YouTube(url)
        if type:
            yt.streams.filter(only_audio=True).first().download()
        else:
            yt.streams.filter(only_audio=False).first().download()
        return {'msg':'Download finished'}
    except Exception as e:
        return {"msg": "Download error", "error":  e}
    
@app.get('/playlist')
def get_videos_from_playlist(url:str):
    try:
        playlist = Playlist(url)
        videos = []
        for i in playlist.video_urls:
            yt = YouTube(i)
            videos.append({
                'title':yt.title,
                'duration':yt.length, 
                'url': i, 
                'thumbnail': yt.thumbnail_url, 
                'author': yt.author
                })
        return  {'msg': 'Playlist Loaded','title': playlist.title, 'total_videos':len(videos), 'videos':videos }
    except Exception as e:
        return {"msg": "Download error", "error": e}

@app.post('/playlist-donwload')
def  playlist_from_url(url:str, type: bool):
    try:
        pl = Playlist(url)
        videos = []
        for video in pl:
            video_result = YouTube(video)
            print(f'Downloading {pl.title}')
            print(video)
            if type:
                video_result.streams.filter(only_audio=True).first().download(f'./{pl.title}')
            else:
                video_result.streams.filter(only_audio=False).first().download(f'./{pl.title}')
            videos.append(video);
        return {"msg":"Playlist Loaded","videos":videos,"total":len(videos)}
    except Exception as e:
        return {"msg": "Download error", "error":  e}

    


