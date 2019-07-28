import youtube_dl
import logging
import os

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger(__name__)

class ThisLogger(object):
    def debug(self, msg):
        log.debug(msg)

    def warning(self, msg):
        log.warning(msg)

    def error(self, msg):
        log.error(msg)

class Downloader:
    def __init__(self, download_folder):
        self.d1 = youtube_dl.YoutubeDL(self.getOptions())
        self.download_folder = download_folder    

    def hook(self, d):
        if d['status'] == 'finished':
            log.debug('Done downloading, converting now.')

    def getOptions(self):
        return {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'restrictfilenames': True,
            'outtmpl': '{}%(title)s-%(id)s.%(ext)s'.format(self.download_folder),
            'logger': ThisLogger(),
            'progress_hooks': [self.hook],
        }

    def startDownloading(self, youtube_url):
        self.d1.download([youtube_url])
