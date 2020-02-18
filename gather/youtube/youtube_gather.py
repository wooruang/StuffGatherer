from pytube import YouTube
from gather.gather import Gather


class YoutubeGather(Gather):
    def __init__(self, src):
        super().__init__(src)

    def streams(self):
        return YouTube(self.src).streams.all()
