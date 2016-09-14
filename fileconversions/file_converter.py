import mimetypes
from . import conversions

class FileConverter(object):

    def get_conversion(self, source_path, format):

        source_mimetype = mimetypes.guess_type(source_path)[0]

        if source_mimetype is None:
            return None

        cls = {
            'application/pdf': conversions.NoOp,
            'image/jpeg': conversions.JpegToPdf,
            'image/png': conversions.PngToPdf,
            'image/gif': conversions.GifToPdf,
            'image/tiff': conversions.TiffToPdf,
            'text/plain': conversions.TextToPdf,
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document': conversions.DocxToPdf,
        }[source_mimetype]


        c = cls()
        c.prepare(source_path)

        return c
