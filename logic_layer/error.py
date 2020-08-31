class InvalidColumnName(Exception):
    def __init__(self, column_name, schema):
        self.column_name = column_name
        self.schema = schema
        self.message = f"invalid column name {self.column_name} for schema {self.schema}"
        super().__init__(self.message)


class InvalidSchema(Exception):
    def __init__(self, schema):
        self.schema = schema
        self.message = f"invalid schema {self.schema}. A schema is a list of tuples"
        super().__init__(self.message)

