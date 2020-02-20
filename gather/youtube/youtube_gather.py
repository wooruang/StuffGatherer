from pytube import YouTube
from gather.gather import Gather


class YoutubeGather(Gather):
    """Download videos in Youtube.

    Parameters
    ------------
    src : str
        Source URL.
    video : bool
    resolution : str
        video's resolution. default is 'highest'
    subtype: str
        Video's subtype. example) 'mp4', 'webm'
    audio : bool
    """
    ARG_VIDEO = 'video'
    ARG_RESOLUTION = 'resolution'
    ARG_SUBTYPE = 'subtype'

    ARG_AUDIO = 'audio'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tube = YouTube(self.src)
        self.video = kwargs[self.ARG_VIDEO] if self.ARG_VIDEO in kwargs else True
        self.resolution = kwargs[self.ARG_RESOLUTION] if self.ARG_RESOLUTION in kwargs else 'highest'
        self.subtype = kwargs[self.ARG_SUBTYPE] if self.ARG_SUBTYPE in kwargs else 'mp4'
        self.audio = kwargs[self.ARG_AUDIO] if self.ARG_AUDIO in kwargs else False
        self.stream = self.select()

    def select(self):
        stream = None
        if self.video and self.audio:
            if self.resolution == 'highest':
                stream = self.tube.streams.get_highest_resolution()
            else:
                stream = self.tube.streams.filter(progressive=True, subtype=self.subtype,
                                                  resolution=self.resolution) \
                    .first()
        elif self.video:
            if self.resolution == 'highest':
                stream = self.tube.streams.filter(adaptive=True, only_video=self.video, subtype=self.subtype) \
                    .order_by("resolution").last()
            else:
                stream = self.tube.streams \
                    .filter(adaptive=True, only_video=self.video, subtype=self.subtype, resolution=self.resolution) \
                    .first()
        else:
            stream = self.tube.streams.filter(adaptive=True, only_audio=self.audio).first()
        return stream

    def streams(self):
        return self.tube.streams

    def download(self, output_path=None):
        """Download youtube's media."""
        print(self.stream)
        return self.stream.download(output_path=output_path)

    def default_file_name(self):
        return self.stream.default_filename
