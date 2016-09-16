from .command_conversion import CommandConversion


class JpegToPdf(CommandConversion):
    command_name = 'convert'
    output_extension = 'pdf'
