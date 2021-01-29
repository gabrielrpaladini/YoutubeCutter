import pytube

class DownloadVideo:

    def __init__(self, url):

        self.download_folder = 'downloads/'
        self.url = url
        self.youtube = pytube.YouTube(self.url)
        self.video = self.youtube.streams.get_highest_resolution()

    def download(self):
        
        self.video.download(self.download_folder)

    def returntitle(self):

        return self.video.title