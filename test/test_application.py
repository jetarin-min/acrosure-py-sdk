# -*- coding: utf-8 -*-

import unittest
from acrosure_sdk import AcrosureClient

from .constants import TEST_SECRET_KEY

class ApplicationTestCase(unittest.TestCase):

    def setUp( self ):
        self.client = AcrosureClient(TEST_SECRET_KEY)
    
    def test_instance_of_acrosure( self ):
        client = self.client
        application = self.client.application
        self.assertIsInstance(client, AcrosureClient)

if __name__ == '__main__':
    unittest.main()

