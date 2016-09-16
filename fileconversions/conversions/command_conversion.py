import subprocess
from .conversion import Conversion
from ..helpers import replace_extension


class CommandConversion(Conversion):

    command_name = None
    output_extension = None
    output_flag = False

    def __call__(self, source_path):
        target_path = replace_extension(self.output_extension, source_path)

        if self.output_flag:
            args = [self.command_name, source_path, '-o', target_path]

        else:
            args = [self.command_name, source_path, target_path]


        rt = subprocess.check_call(args)

        return [target_path]
