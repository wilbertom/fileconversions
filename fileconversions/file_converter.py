from .conversions import NoOpConversion, PngToPdfConversion, \
    JpegToPdfConversion, GifToPdfConversion, TiffToPdfConversion, \
    TextToPdfConversion
import mimetypes


class FileConverter(object):

    def get_conversion(self, source_path, format):

        source_mimetype = mimetypes.guess_type(source_path)[0]

        cls = {
            'application/pdf': NoOpConversion,
            'image/jpeg': JpegToPdfConversion,
            'image/png': PngToPdfConversion,
            'image/gif': GifToPdfConversion,
            'image/tiff': TiffToPdfConversion,
            'text/plain': TextToPdfConversion,
        }[source_mimetype]


        c = cls()
        c.prepare(source_path)

        return c
