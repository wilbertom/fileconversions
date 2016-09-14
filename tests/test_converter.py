import unittest
from fileconversions import FileConverter, FileFormats
from fileconversions.conversions import NoOpConversion


class TestConverter(unittest.TestCase):

    def setUp(self):
        super(TestConverter, self).setUp()
        self.converter = FileConverter()

    def assertIsConversion(self, c, cls):
        self.assertIsInstance(c, cls)

    def test_getting_pdf_to_pdf_conversion(self):
        conversion = self.converter.get_conversion('hello.pdf', FileFormats.PDF)
        self.assertIsConversion(conversion, NoOpConversion)
        # we can run it without any issues because it doesn't do anything
        conversion.run()
