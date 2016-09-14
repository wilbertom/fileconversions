from .conversion import Conversion


class NoOpConversion(Conversion):

    def run(self):
        pass