class Gather:
    def __init__(self, **kwargs):
        self.src = kwargs['src'] if 'src' in kwargs else None
        pass

    def streams(self):
        pass

    def download(self, output_dir):
        pass
