from .command_conversion import CommandConversion


class TiffToPdf(CommandConversion):
    command_name = 'tiff2pdf'
    output_extension = 'pdf'
    output_flag = True
