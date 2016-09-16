from .conversion import Conversion


class NoOp(Conversion):

    def __call__(self, source_path):
        pass
