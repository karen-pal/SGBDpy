from error import InvalidSchema
import os
dirname = os.path.dirname(__file__)

import schema
class Table:
    def __init__(self, schema, tablename):
        self.schema = self.validated_schema(schema)
        self.tablename = tablename.lower()
        self.file = self.new_file()

    @staticmethod
    def validated_schema(raw_schema):
        """
        schema es una lista de tuplas
        """
        if type(raw_schema) is not list:
            raise InvalidSchema(raw_schema)
        else:
            for elem in raw_schema:
                if type(elem) is not tuple:
                    raise InvalidSchema(raw_schema)
            return schema.Schema(raw_schema)

    def new_file(self):
        filename = dirname+ "/data/"+ self.tablename + ".stol" #table in croatian
        f = open(filename, "w")
        f.write(str(self.schema))
        f.close()
        return filename
