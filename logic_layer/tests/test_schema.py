import sys
import unittest

sys.path.append("../")


import schema
import column


class TestColumn(unittest.TestCase):
    def test_create_column(self):
        new_column = column.Column("Nombre", "string(10)")
        self.assertEqual(new_column.column_name, "nombre")
        self.assertEqual(new_column.column_type, ("string", 10))


class TestSchema(unittest.TestCase):
    def test_create_schema(self):
        new_schema = schema.Schema([("id", "int(3)"), ("NOmbre", "string(10)")])
        self.assertEqual(len(new_schema.columns), 2)

        self.assertEqual(new_schema.columns[0].column_type, ("int", 3))


if __name__ == "__main__":
    unittest.main()
