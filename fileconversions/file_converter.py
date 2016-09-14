import mimetypes
from .conversions import NoOpConversion, PngToPdfConversion, \
    JpegToPdfConversion, GifToPdfConversion, TiffToPdfConversion, \
    TextToPdfConversion, DocxToPdfConversion


class FileConverter(object):

    def get_conversion(self, source_path, format):

        source_mimetype = mimetypes.guess_type(source_path)[0]

        if source_mimetype is None:
            return None

        cls = {
            'application/pdf': NoOpConversion,
            'image/jpeg': JpegToPdfConversion,
            'image/png': PngToPdfConversion,
            'image/gif': GifToPdfConversion,
            'image/tiff': TiffToPdfConversion,
            'text/plain': TextToPdfConversion,
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document': DocxToPdfConversion,
        }[source_mimetype]


        c = cls()
        c.prepare(source_path)

        return c
