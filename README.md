# YouTube Video Downloader & Converter
Dies ist ein Python-Skript, das verwendet werden kann, um YouTube-Videos herunterzuladen und sie automatisch in das MP3-Format zu konvertieren. 
- Das Skript liest die URLs der YouTube-Videos aus einer Textdatei (videos.txt) und speichert die heruntergeladenen Videos im MP4-Format in einem separaten Ordner.
- Dann wird jedes Video in das MP3-Format konvertiert und im MP3-Ordner gespeichert.

## Anleitung
Installiere die erforderlichen Bibliotheken, wenn sie noch nicht installiert sind:
```py
pip install pytube moviepy
```

Füge die URLs der YouTube-Videos in "videos.txt" ein, die du herunterladen und konvertieren möchtest. Stelle sicher, dass jede URL in einer neuen Zeile steht.

Passe die Pfade output_folder_mp4 und output_folder_mp3 in der Python-Datei entsprechend an, um die Ordner festzulegen, in denen die heruntergeladenen MP4- und konvertierten MP3-Dateien gespeichert werden sollen:
```py
output_folder_mp4 = "pfad/für/mp4"
output_folder_mp3 = "pfad/für/mp3"
```

Führe das Python-Skript aus:
```py
python youtube_downloader.py
```
Das Skript wird die Videos gemäß den URLs in der "videos.txt"-Datei herunterladen, sie in MP4-Format speichern und dann in MP3-Format konvertieren.

## Hinweise
Stelle sicher, dass du die Nutzungsbedingungen von YouTube befolgst und nur Videos herunterlädst, die du für den persönlichen Gebrauch oder im Einklang mit den YouTube-Richtlinien verwenden darfst.

Wenn du weitere URLs in der "videos.txt"-Datei hinzufügst, wird das Skript automatisch die neuen Videos herunterladen und konvertieren, wenn du es erneut ausführst.

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die [LICENSE-Datei](https://github.com/max5695/YouTubeDownloader/blob/main/LICENSE) für weitere Informationen.
