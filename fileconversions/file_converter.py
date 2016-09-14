from .conversions import NoOpConversion, PngToPdfConversion, \
    JpegToPdfConversion
import mimetypes


class FileConverter(object):

    def get_conversion(self, source_path, format):

        source_mimetype = mimetypes.guess_type(source_path)[0]

        cls = {
            'application/pdf': NoOpConversion,
            'image/png': PngToPdfConversion,
            'image/jpeg': JpegToPdfConversion,

        }[source_mimetype]


        c = cls()
        c.prepare(source_path)

        return c
