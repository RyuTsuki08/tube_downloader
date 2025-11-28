# 🚀 Aplicación de Python para descargar videos de YouTube

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)

</div>

Esta es una sencilla aplicación de Python para descargar videos de YouTube.

## Requisitos
---------

1. Python 3: https://www.python.org/downloads/
2. Pip (incluido en la distribución de Python): https://pip.pypa.io/en/stable/installing/
3. Kitty (terminal) - Opcional
4. Git - Control de versiones
5. Node-js y npm (para el frontend)

## Instalación
------------

1. Clone el repositorio, usando:
```sh copy code
git clone https://github.com/RyuTsuki08/tube_downloader.git && cd tube_downloader
```

2. Luego, si quiere ahorrar todo el proceso de instalación solo asegurese de tener instalado los programas mencionados anteriormente y copie esto:
```sh copy code
sudo chmod +x ./install.sh 
```

3. Ejecute el script "./install.sh" con permisos de superusuario:
```sh copy code
./install.sh
```

### Instalación manual 
------------------

Si prefiere no usar un script de instalación, puede seguir los siguientes pasos:

1. Al clonar este repositorio, deberá iniciar el entorno virtual: 
```sh copy code
source tube/bin/activate
# En Windows: venv\Scripts\activate
```

2. Instala las dependencias de Python usando el archivo 'requirements.txt':
```sh copy code
pip install -r requirements.txt
```

3. Luego ejecute el backend de 'fastapi' con 'uvicorn':
```sh copy code
uvicorn main:app --reload
```

## Probando la aplicación
----------------------

Si todo inició sin error podrás probar la aplicación desde una terminal, ejecutando el siguiente comando:

```sh copy code
curl -X GET 'http://127.0.0.1:8000/?url=https://www.youtube.com/watch?v=9bZkp7q19f0'
```

Esto debería devolver una respuesta como: 
```json
{"msg":"Video loaded successfuly","video":{"id":"9bZkp7q19f0","url":"https://www.youtube.com/watch?v=9bZkp7q19f0","tile":"Gangnam Style","thumbnail":"https://i.ytimg.com/vi/9bZkp7q19f0/hq720.jpg...","author":"PSY"}}
```

**NOTA:**
Este es el backend de una aplicación web que puede descargar vídeos y playlists de youtube. El frontend se encuentra en otro repositorio: [Frontend](https://github.com/RyuTsuki08/tube_downloader_frontend). El script `install.sh` cuenta con los comando para ejecutar el frontend. Pero también puedes ejecutar ambos lados aparte, depende de como prefieras usar la aplicación.

## Desconexión
-----------

Para salir del entorno virtual de Python, ejecuta el siguiente comando:

`deactivate`

## Contribuyendo
-------------

Por favor, contribuye con el desarrollo de esta aplicación de Python. Si tienes ideas de cómo mejorar este script, envía una solicitud de extracción en GitHub.

## 👨‍💻 Desarrollador

**Christian Paez**

<div align="left">
  <a href="https://github.com/RyuTsuki08" target="_blank">
    <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/christian-paez-3b6b7b1b3/" target="_blank">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://www.instagram.com/christianpaez_/" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white" alt="Instagram">
  </a>
</div>

## Licencia
-----------
MIT License 
Esta aplicación de Python para descargar videos de YouTube está bajo licencia MIT.

¡Gracias por utilizar esta aplicación de Python!
