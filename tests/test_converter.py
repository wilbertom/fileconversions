import unittest
from fileconversions import FileConverter, FileFormats
from fileconversions.conversions.conversion import Conversion
from fileconversions.conversions import NoOpConversion, PngToPdfConversion, \
    JpegToPdfConversion


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
            'hello.jpeg', FileFormats.PDF, JpegToPdfConversion
        )
