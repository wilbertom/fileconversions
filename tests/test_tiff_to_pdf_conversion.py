from fileconversions.testing import ConversionTestCase
from fileconversions.conversions import TiffToPdf


class TestTiffToPdfConversion(ConversionTestCase):
    conversion_cls = TiffToPdf

    def test_command_is_installed(self):
        self.assertCommandExists(self.conversion.command_name)

