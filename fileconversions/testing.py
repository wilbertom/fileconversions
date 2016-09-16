import unittest
import subprocess


class ConversionTestCase(unittest.TestCase):

    conversion_cls = None


    def setUp(self):
        super(ConversionTestCase, self).setUp()
        self.conversion = self.conversion_cls()
        self.null = open('/dev/null', 'w')

    def tearDown(self):
        super(ConversionTestCase, self).tearDown()
        self.null.close()

    def assertCommandExists(self, command):
        rt = subprocess.call(['which', command], stdout=self.null)
        self.assertEquals(rt, 0, 'Command {} not found'.format(command))
