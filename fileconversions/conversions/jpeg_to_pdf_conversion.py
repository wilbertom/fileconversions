import subprocess
from .conversion import Conversion
from ..helpers import replace_extension


class JpegToPdf(Conversion):

    def __call__(self, source_path):
        target_path = replace_extension('pdf', source_path)

        rt = subprocess.check_call([
            'convert',
            source_path,
            target_path
        ])

        return target_path
