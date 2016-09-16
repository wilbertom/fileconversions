from .helpers import mimetype_for


class FileFormats(object):
    PDF = mimetype_for('pdf')
    JPEG = mimetype_for('jpeg')
    PNG  = mimetype_for('png')
    GIF  = mimetype_for('gif')
    TIFF = mimetype_for('tiff')
    TXT  = mimetype_for('txt')
    DOCX = mimetype_for('docx')
    DOC  = mimetype_for('doc')
    PPTX = mimetype_for('pptx')
    PPT  = mimetype_for('ppt')
    ODT  = mimetype_for('odt')
    RTF  = mimetype_for('rtf')
