## Aplicación de Python para descargar videos de YouTube ##
Esta es una sencilla aplicación de Python para descargar videos de YouTube. 

Requisitos
---------

El proyecto ahorita esta disponible solo para sistemas operativos GNU/linux

1. Python 3: https://www.python.org/downloads/
2. Pip (incluido en la distribución de Python): https://pip.pypa.io/en/stable/installing/
3. Kitty (terminal)
4. Git - Control de versiones
5. Node-js y npm



Instalación
------------
1. Clone el repositorio,  usando:
```sh copy code
git clone https://github.com/RyuTsuki08/tube_downloader.git && cd  tube_downloader
```
2. Luego, si quiere ahorrar todo el proceso de instalación solo asegurese de tener instalado los programas  mencionados anteriormente y copie esto:
``` sh copy code
sudo chmod +x ./install.sh 
```
3. Ejecute el script "./install.sh" con permisos de superusuario:
```sh copy code
./install.sh
 ```

Instalación manual 
------------------
Si prefiere no usar un script de instalación, puede seguir los siguientes pasos:
1. Al clonar  este repositorio, deberá iniciar el entorno virtual: 
```sh copy code
source tube/bin/activate
```
2. Instala las dependencias de Python usando el archivo 'requirements.txt':
```sh copy code
pip install -r requirements.txt
```
3. Luego ejecute el backend de 'fastapi' con 'uvicorn':
```sh copy code
uvicorn  main:app --reload
```

Probando la aplicación
----------------------

Si todo inició sin error podrás probar la aplicación desde una terminal, ejecutando el siguiente comando:
```sh copy code

curl -X GET 'http://127.0.0.1:8000/?url=https://www.youtube.com/watch?v=9bZkp7q19f0'

```

Esto debería devolver una respuesta como: 
```sh 
{"msg":"Video loaded successfuly","video":{"id":"9bZkp7q19f0","url":"https://www.youtube.com/watch?v=9bZkp7q19f0","tile":"Gangnam Style","thumbnail":"https://i.ytimg.com/vi/9bZkp7q19f0/hq720.jpg?sqp=-oaymwEXCNUGEOADIAQqCwjVARCqCBh4INgESFo&rs=AOn4CLDGWPq_kk5PtRvI00NrQRRwVOVYnA","author":"PSY"}}
```

NOTA:
Este es el backend de una aplicación web que puede descargar vídeos y playlists de youtube . El frontend se encuentra en otro repositorio: [Frontend](https://github.com/RyuTsuki08/tube_downloader_frontend). El script `install.sh` cuenta con los comando para ejecutar el frontend. Pero también puedes ejecutar ambos lados aparte, depende de como prefieras usar la aplicación. 

Desconexión
-----------
Para salir del entorno virtual de Python, ejecuta el siguiente comando:

`deactivate`

Contribuyendo
-------------

Por favor, contribuye con el desarrollo de esta aplicación de Python. Si tienes ideas de cómo mejorar este script, envía una solicitud de extracción en GitHub.

Licencia
-----------
MIT License 
Esta aplicación de Python para descargar videos de YouTube está bajo licencia MIT.

¡Gracias por utilizar esta aplicación de Python!

