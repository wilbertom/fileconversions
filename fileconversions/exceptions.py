

class FileConversionsException(Exception):
    """
    Root exception for exceptions created in this library.

    """
    pass


class ConversionException(FileConversionsException):
    """
    Raised when a file conversion error occurs.

    """
    pass
