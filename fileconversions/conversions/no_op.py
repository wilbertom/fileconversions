from .conversion import Conversion


class NoOp(Conversion):

    def run(self):
        pass