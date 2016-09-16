from fileconversions.testing import ConversionTestCase
from fileconversions.conversions import TextToPdf


class TestTextToPdfConversion(ConversionTestCase):
    conversion_cls = TextToPdf

    def test_command_is_installed(self):
        self.assertCommandExists(self.conversion.command_name)

