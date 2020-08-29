import unittest
import schema
import column


class TestColumn(unittest.TestCase):
    def test_create_column(self):
        column = column.Column("Nombre", "string(10)")
        self.assertEqual(column.column_name, "nombre")
        self.assertEqual(column.column_type, ("string", 10))


class TestSchema(unittest.TestCase):
    def test_create_schema(self):
        new_schema = schema.Schema([("id", "int(3)"), ("NOmbre", "string(10)")])
        self.assertEqual(len(new_schema.columns), 2)

        self.assertEqual(new_schema.columns[0].column_type, ("int", 3))


if __name__ == "__main__":
    unittest.main()
