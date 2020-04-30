# Descargar live de instagram. 

Anteriormente descargaba los live con [IG Stories for chrome](https://chrome.google.com/webstore/detail/ig-stories-for-instagram/nilbfjdbacfdodpbdondbbkmoigehodg), pero ahora la bloquea el antivirus. Entonces decidi hacer algo, pero como aun no se como obtener las url de los videos, debo seguir usando esta extensión. 

## Prerequisitos
```
pip install  click
pip install  wget
pip install  mhmovie
```

Descargar [Ffmpeg](https://www.ffmpeg.org/) y agregar la carpeta bin al path

## Como obtener los link
1. Ver el live con la extension y presionar en download y despues "Get Downloader", el antivirus lo va a bloquer, pero van a descargas y copian el link desde donde intento descargarlo.
2. El link lo copian en un archivo, como en el ejemplo (links.txt)
3. Pueden agregar la cantidad de link que deseen. 

## Ejecutar 
```
python download.py --file=D:\links.txt  --output=E:\output
```

Para ayuda 
```
python download --help
```