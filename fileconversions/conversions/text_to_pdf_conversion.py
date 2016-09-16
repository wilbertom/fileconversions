import subprocess
from .conversion import Conversion
from ..helpers import replace_extension


class TextToPdf(Conversion):

    def __call__(self, source_path):
        target_path = replace_extension('pdf', source_path)

        rt = subprocess.check_call([
            'pandoc',
            source_path,
            '-o',
            target_path
        ])

        return [target_path]
