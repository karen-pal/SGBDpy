import os

dirname = os.path.dirname(__file__)


import unittest
import sys

sys.path.append("../")

import table


class TestTable(unittest.TestCase):
    def test_table_creation(self):
        new_table = table.Table(
            schema=[("id", "int(3)"), ("nOmbre", "string(10)")], tablename="Personas"
        )
        self.assertEqual(new_table.tablename, "personas")
        self.assertTrue("/data/personas.stol" in new_table.phys_link)

    def test_table_file_content(self):
        new_table = table.Table(
            schema=[("id", "int(3)"), ("nOmbre", "string(10)")], tablename="Personas2"
        )
        f = open(new_table.phys_link)
        content = f.read()
        print(content)
        f.close()
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
