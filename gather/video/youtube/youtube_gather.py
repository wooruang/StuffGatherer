from pytube import YouTube
from pytube import query
from gather.video.gather import Gather


class YoutubeGather(Gather):
    """Download videos in Youtube.

    Parameters
    ------------
    src : str
        Source URL.
    """

    def __init__(self, src):
        super().__init__(src)
        self.tube = YouTube(self.src)

    def get_streams(self, video=True, audio=True, subtitle=True):
        if video and audio and subtitle:
            return self.tube.streams
        elif video and audio:
            return self.tube.streams.filter()
        elif video and not audio:
            return self.tube.streams.filter()
        elif audio and not video:
            return self.tube.streams.filter()
        else:
            return query.StreamQuery(list())

    @staticmethod
    def download(stream, output_path=None):
        """Download youtube's media."""
        return stream.download(output_path=output_path)

    @staticmethod
    def get_default_file_name(stream):
        return stream.default_filename
