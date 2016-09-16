from . import conversions
from .file_formats import FileFormats


class FileConverter(object):

    def get_conversion(self, source_format, target_format):

        return {
            FileFormats.PDF: conversions.NoOp,
            FileFormats.JPEG: conversions.JpegToPdf,
            FileFormats.PNG: conversions.PngToPdf,
            FileFormats.GIF: conversions.GifToPdf,
            FileFormats.TIFF: conversions.TiffToPdf,
            FileFormats.TXT: conversions.TextToPdf,
            FileFormats.DOCX: conversions.DocxToPdf,
            FileFormats.DOC: conversions.DocToPdf,
            FileFormats.PPTX: conversions.PptxToPdf,
            FileFormats.PPT: conversions.PptToPdf,
            FileFormats.ODT: conversions.OdtToPdf,
            FileFormats.RTF: conversions.RtfToPdf,
        }[source_format]()
