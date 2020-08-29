import unittest

import table

class TestTable(unittest.TestCase):

    def test_table_creation(self):
        new_table = table.Table(schema=[("id","int(3)"),("nOmbre","string(10)")],tablename="Personas")
        self.assertEqual(new_table.tablename,"personas")
        self.assertEqual(new_table.file, "./data/personas.stol")
    def test_table_file_content(self):
        new_table = table.Table(schema=[("id","int(3)"),("nOmbre","string(10)")],tablename="Personas2")
        f = open(new_table.file)
        content = f.read()
        print(content)
        f.close()
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
