import os
import urllib.parse as urlparse
from os import path
from urllib.parse import parse_qs

import click
import wget
from mhmovie.code import *

#TODO: Leer el archivo de links como csv y al archivo agregarle una columna
    #  con el nombre de salida del archivo. 
def validate_folder(folder):
    if not path.exists(folder):
        os.mkdir(folder) 

def download(path, output=os.path.join(os.getcwd(),"output")):
    validate_folder(output)
    
    __file = wget.download(path, out=output)
    return (__file)

def change_extension(path):
    base = os.path.splitext(path)[0]
    new_file = os.rename(path, base + '.mp3')
    return (base + '.mp3')

@click.command()
@click.option('--file', default=None,  help='path file with links to download ig live')
@click.option('--output', default=os.path.join(os.getcwd(),"output"),  help='folder to save join video')
def read_file_with_link(file, output):
    import csv
    with open(file, encoding="utf-8") as __file:
        links = csv.reader(__file, delimiter=',')
        for pos , row in enumerate(links):
           data_url = urlparse.urlparse(urlparse.unquote(row[0])).query
           paths = data_url.split('file_v=')[1].split('&file_a=')
           join_video = os.path.join(output,  row[1] + ".mp4")
           file_video = download(paths[0], output)
           file_audio = change_extension(download(paths[1], output))
           join_audio_and_video(file_audio, file_video, join_video)
           os.remove(file_video)
           os.remove(file_audio)
def join_audio_and_video(audio, video, save):
    m = movie(video)
    mu = music(audio)
    mu.Aconvert()
    final = m+mu
    final.save(save)


if __name__ == "__main__":
    read_file_with_link()


