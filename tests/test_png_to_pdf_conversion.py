from fileconversions.testing import ConversionTestCase
from fileconversions.conversions import PngToPdf


class TestPngToPdfConversion(ConversionTestCase):
    conversion_cls = PngToPdf

    def test_command_is_installed(self):
        self.assertCommandExists(self.conversion.command_name)

