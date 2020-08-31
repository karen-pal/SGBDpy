import sys
import unittest
import os

sys.path.append("../")


import schema
import column
import database

class TestDatabase(unittest.TestCase):
    def create_database(self):
        test_db_name = 'test_db'
        db = database.Database(name=test_db_name)
        self.assertTrue(os.path.isdir('./storage_layer/data/'+test_db_name))
