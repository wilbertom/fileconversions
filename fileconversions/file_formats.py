

class FileFormat(object):

    def __init__(self, extension, mime_types):
        self.mimetypes = mime_types
        self.default_extension = extension


class FileFormats(object):

    PDF = FileFormat(
        'pdf',
        ['application/pdf']
    )
