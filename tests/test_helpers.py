import unittest
import fileconversions.helpers


class TestHelpers(unittest.TestCase):

    def test_dropping_simple_file_extension(self):

        self.assertEquals(
            fileconversions.helpers.drop_extension('hello.txt'),
            'hello'
        )

    def test_dropping_extension_when_there_are_two_dots(self):

        self.assertEquals(
            fileconversions.helpers.drop_extension('hello.txt.pdf'),
            'hello.txt'
        )

    def test_new_extension(self):
        self.assertEquals(
            fileconversions.helpers.replace_extension('pdf', 'hello.txt'),
            'hello.pdf'
        )

    def test_new_extension_with_two_dots(self):
        self.assertEquals(
            fileconversions.helpers.replace_extension('pdf', 'hello.txt.jpg'),
            'hello.txt.pdf'
        )
