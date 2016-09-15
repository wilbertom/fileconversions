

def drop_extension(filepath):
    index = filepath.rindex('.')
    return filepath[0:index]


def replace_extension(extension, filepath):
    return '{}.{}'.format(drop_extension(filepath), extension)
