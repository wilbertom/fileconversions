from . import conversions
from .file_formats import FileFormats


class FileConverter(object):

    def get_conversion(self, source_format, target_format):

        return {
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
        }[source_format]()
