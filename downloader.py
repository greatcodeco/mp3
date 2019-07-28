import youtube_dl


class Downloader:
    def __init__(self):
        self.d1 = youtube_dl.YoutubeDL(self.getOptions())

    def hook(self, d):
        if d['status'] == 'finished':
            print('Done downloading, converting now.')

    def getOptions(self):
        return {
            'outtmpl': 'mp3_files/ilteris.mp3',
            'format': 'bestaudio/best',
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
            'progress_hooks': [self.hook],
        }

    def startDownloading(self, youtube_url):
        self.d1.download([youtube_url])
