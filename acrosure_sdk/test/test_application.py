# -*- coding: utf-8 -*-

import unittest
from ..client import AcrosureClient
from ..application import ApplicationManager

from .constants import TEST_SECRET_KEY

class ApplicationTestCase(unittest.TestCase):

    def setUp( self ):
        self.client = AcrosureClient(TEST_SECRET_KEY)
    
    def test_instance_of_acrosure( self ):
        client = self.client
        application = self.client.application
        self.assertIsInstance(client, AcrosureClient)
        self.assertIsInstance(application, ApplicationManager)

if __name__ == '__main__':
    unittest.main()

