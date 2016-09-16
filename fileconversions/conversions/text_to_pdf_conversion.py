from .command_conversion import CommandConversion


class TextToPdf(CommandConversion):

    command_name = 'pandoc'
    output_extension = 'pdf'
    output_flag = True
