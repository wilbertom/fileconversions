import os
import mimetypes
from . import conversions


# use our own mime types file because not all extensions are supported on all
# linux distros
mime_types_file = os.path.join(os.path.dirname(__file__), 'mime.types')
mimetypes.init([mime_types_file])


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
            'application/msword': conversions.DocToPdf,
            'application/vnd.openxmlformats-officedocument.presentationml.presentation': conversions.PptxToPdf,
            'application/vnd.ms-powerpoint': conversions.PptToPdf,
            'application/vnd.oasis.opendocument.text': conversions.OdtToPdf,
            'application/rtf': conversions.RtfToPdf,
        }[source_mimetype]


        c = cls()
        c.prepare(source_path)

        return c
