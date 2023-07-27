import os
from pytube import YouTube
from moviepy.editor import *


file_path = "videos.txt"
output_folder_mp4 = "pfad/für/mp4"
output_folder_mp3 = "pfad/für/mp3"


def download_youtube_video_as_mp4(video_url, output_path):
    try:
        # Video-Objekt erstellen
        video = YouTube(video_url)

        # Fortschritt anzeigen
        print("Lade Video herunter: " + video.title)

        # Herunterladen des Videos als MP4
        video_stream = video.streams.get_highest_resolution()
        video_stream.download(output_path)

        print("Herunterladen als MP4 abgeschlossen!")

        # Rückgabe des heruntergeladenen Dateipfads
        return os.path.join(output_path, video_stream.default_filename)

    except Exception as e:
        print("Fehler beim Herunterladen: " + str(e))
        return None

def convert_video_to_mp3(video_path, output_path):
    try:
        # Video-Objekt erstellen
        video = VideoFileClip(video_path)

        # Audio extrahieren und als MP3 speichern
        audio = video.audio
        audio.write_audiofile(output_path)

        print("Konvertierung zu MP3 abgeschlossen!")

    except Exception as e:
        print("Fehler bei der Konvertierung: " + str(e))



try:
    with open(file_path, 'r') as file:
        urls = file.readlines()
        for url in urls:
            # Entferne eventuelle Leerzeichen und Zeilenumbrüche am Anfang oder Ende der URL
            video_url = url.strip()

            # Lade das Video herunter und speichere den Pfad der heruntergeladenen Datei
            downloaded_video_path = download_youtube_video_as_mp4(video_url, output_folder_mp4)

            if downloaded_video_path:
                # Konvertiere das Video zu MP3 und speichere es im MP3-Ordner
                mp3_output_path = os.path.splitext(os.path.basename(downloaded_video_path))[0] + ".mp3"
                mp3_output_path = os.path.join(output_folder_mp3, mp3_output_path)
                convert_video_to_mp3(downloaded_video_path, mp3_output_path)

except Exception as e:
    print("Fehler beim Auslesen der Datei: " + str(e))
