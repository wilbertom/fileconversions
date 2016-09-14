import unittest
from fileconversions import FileConverter, FileFormats
from fileconversions.conversions.conversion import Conversion
from fileconversions.conversions import NoOpConversion, PngToPdfConversion, \
    JpegToPdfConversion, GifToPdfConversion, TiffToPdfConversion, \
    TextToPdfConversion, DocxToPdfConversion


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
            'hello.pdf', FileFormats.PDF, NoOpConversion
        )

    def test_getting_png_to_pdf_conversion(self):
        self.assertGettingConversion(
            'hello.png', FileFormats.PDF, PngToPdfConversion
        )

    def test_getting_jpg_to_pdf_conversion(self):
        self.assertGettingConversion(
            'hello.jpg', FileFormats.PDF, JpegToPdfConversion
        )

    def test_getting_jpeg_to_pdf_conversion(self):
        self.assertGettingConversion(
            'hello.jpeg', FileFormats.PDF, JpegToPdfConversion
        )

    def test_getting_gif_to_pdf_conversion(self):
        self.assertGettingConversion(
            'hello.gif', FileFormats.PDF, GifToPdfConversion
        )

    def test_getting_tiff_to_pdf_conversion(self):
        self.assertGettingConversion(
            'hello.tiff', FileFormats.PDF, TiffToPdfConversion
        )

    def test_getting_text_to_pdf_conversion(self):
        self.assertGettingConversion(
            'hello.txt', FileFormats.PDF, TextToPdfConversion
        )

    def test_getting_docx_to_pdf_conversion(self):
        self.assertGettingConversion(
            'hello.docx', FileFormats.PDF, DocxToPdfConversion
        )
