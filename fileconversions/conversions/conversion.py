import abc


class Conversion(object):

    def __init__(self):
        self._source_path = None

    def prepare(self, source_path):
        self._source_path = source_path
        return self

    @abc.abstractclassmethod
    def run(self):
        raise NotImplementedError
