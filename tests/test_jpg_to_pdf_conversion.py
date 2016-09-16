from fileconversions.testing import ConversionTestCase
from fileconversions.conversions import JpegToPdf


class TestJpgToPdfConversion(ConversionTestCase):
    conversion_cls = JpegToPdf

    def test_command_is_installed(self):
        self.assertCommandExists(self.conversion.command_name)

