import abc


class Conversion(object):

    @abc.abstractclassmethod
    def __call__(self, source_path):
        raise NotImplementedError
