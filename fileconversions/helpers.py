import os
import mimetypes

# use our own mime types file because not all extensions are supported on all
# linux distros
_mime_types_file = os.path.join(os.path.dirname(__file__), 'mime.types')
mimetypes.init([_mime_types_file])


def drop_extension(filepath):
    index = filepath.rindex('.')
    return filepath[0:index]


def replace_extension(extension, filepath):
    return '{}.{}'.format(drop_extension(filepath), extension)


def mimetype(filepath):
    return mimetypes.guess_type(filepath)[0]


def mimetype_for(extension):
    mime = mimetype('mock_file_name.{}'.format(extension))
    # if this is none then one of the fileconversions.FileFormats might result
    # in none, acting as a fallback for unknown extensions
    assert mime is not None

    return mime