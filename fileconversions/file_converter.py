from .conversions import NoOpConversion


class FileConverter(object):

    def get_conversion(self, source_path, format):
        c = NoOpConversion()
        c.prepare(source_path)
        return c
