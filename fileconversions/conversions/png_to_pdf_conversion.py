from .command_conversion import CommandConversion


class PngToPdf(CommandConversion):
    command_name = 'convert'
    output_extension = 'pdf'
