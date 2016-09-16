import unittest
from fileconversions import FileConverter, FileFormats
from fileconversions.conversions.conversion import Conversion
from fileconversions import conversions


class TestConverter(unittest.TestCase):


    def setUp(self):
        super(TestConverter, self).setUp()
        self.converter = FileConverter()

    def assertIsSubClass(self, c1, c2):
        if not issubclass(c1, c2):
            raise AssertionError('{} is not a subclass of {}'.format(
                c1.__name__, c2.__name__
            ))

    def assertIsConversion(self, c, cls):
        self.assertIsInstance(c, cls)
        self.assertIsSubClass(cls, Conversion)

    def assertGettingConversion(self, source_path, file_format, conversion_cls):
        conversion = self.converter.get_conversion(source_path, FileFormats.PDF)
        self.assertIsConversion(conversion, conversion_cls)

    def test_getting_pdf_to_pdf_conversion(self):
        self.assertGettingConversion(
            FileFormats.PDF, FileFormats.PDF, conversions.NoOp
        )

    def test_getting_png_to_pdf_conversion(self):
        self.assertGettingConversion(
            FileFormats.PNG, FileFormats.PDF, conversions.PngToPdf
        )

    def test_getting_jpg_to_pdf_conversion(self):
        self.assertGettingConversion(
            FileFormats.JPEG, FileFormats.PDF, conversions.JpegToPdf
        )

    def test_getting_gif_to_pdf_conversion(self):
        self.assertGettingConversion(
            FileFormats.GIF, FileFormats.PDF, conversions.GifToPdf
        )

    def test_getting_tiff_to_pdf_conversion(self):
        self.assertGettingConversion(
            FileFormats.TIFF, FileFormats.PDF, conversions.TiffToPdf
        )

    def test_getting_text_to_pdf_conversion(self):
        self.assertGettingConversion(
            FileFormats.TXT, FileFormats.PDF, conversions.TextToPdf
        )

    def test_getting_docx_to_pdf_conversion(self):
        self.assertGettingConversion(
            FileFormats.DOCX, FileFormats.PDF, conversions.DocxToPdf
        )

    def test_getting_doc_to_pdf_conversion(self):
        self.assertGettingConversion(
            FileFormats.DOC, FileFormats.PDF, conversions.DocToPdf
        )

    def test_getting_pptx_to_pdf_conversion(self):
        self.assertGettingConversion(
            FileFormats.PPTX, FileFormats.PDF, conversions.PptxToPdf
        )

    def test_getting_ppt_to_pdf_conversion(self):
        self.assertGettingConversion(
            FileFormats.PPT, FileFormats.PDF, conversions.PptToPdf
        )

    def test_getting_odt_to_pdf_conversion(self):
        self.assertGettingConversion(
            FileFormats.ODT, FileFormats.PDF, conversions.OdtToPdf
        )

    def test_getting_rtf_to_pdf_conversion(self):
        self.assertGettingConversion(
            FileFormats.RTF, FileFormats.PDF, conversions.RtfToPdf
        )
