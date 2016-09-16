import unittest
from fileconversions.helpers import mimetype


class TestMimetypes(unittest.TestCase):

    def test_pdf_mimetype(self):
        self.assertEquals(
            mimetype('hello.pdf'),
            'application/pdf'
        )

    def test_jpeg_mimetype(self):
        self.assertEquals(
            mimetype('hello.jpeg'),
            'image/jpeg'
        )

        self.assertEquals(
            mimetype('hello.jpg'),
            'image/jpeg'
        )

    def test_png_mimetype(self):
        self.assertEquals(
            mimetype('hello.png'),
            'image/png'
        )

    def test_gif_mimetype(self):
        self.assertEquals(
            mimetype('hello.gif'),
            'image/gif'
        )

    def test_tiff_mimetype(self):
        self.assertEquals(
            mimetype('hello.tiff'),
            'image/tiff'
        )

    def test_text_mimetype(self):
        self.assertEquals(
            mimetype('hello.txt'),
            'text/plain'
        )

    def test_docx_mimetype(self):
        self.assertEquals(
            mimetype('hello.docx'),
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

    def test_doc_mimetype(self):
        self.assertEquals(
            mimetype('hello.doc'),
            'application/msword'
        )

    def test_pptx_mimetype(self):
        self.assertEquals(
            mimetype('hello.pptx'),
            'application/vnd.openxmlformats-officedocument.presentationml.presentation'
        )

    def text_ppt_mimetype(self):
        self.assertEquals(
            mimetype('hello.ppt'),
            'application/vnd.ms-powerpoint'
        )

    def text_odt_mimetype(self):
        self.assertEquals(
            mimetype('hello.odt'),
            'application/vnd.oasis.opendocument.text'
        )

    def text_rtf_mimetype(self):
        self.assertEquals(
            mimetype('hello.rtf'),
            'application/rtf'
        )
