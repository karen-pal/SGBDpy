from error import InvalidSchema
import os

dirname = os.path.dirname(__file__)
from . import schema
from storage_layer import storage


class Table:
    def __init__(self, *, schema, tablename, db):
        self.schema = self.validated_schema(schema)
        self.tablename = tablename.lower()
        self.phys_link = self.create_phys_link() #self.new_file()
        self.db = db

    @staticmethod
    def validated_schema(raw_schema):
        """
        schema is a list of tuples
        """
        if type(raw_schema) is not list:
            raise InvalidSchema(raw_schema)
        else:
            for elem in raw_schema:
                if type(elem) is not tuple:
                    raise InvalidSchema(raw_schema)
            return schema.Schema(raw_schema)

    def create_phys_link(self):
        """
        pass this task to the storage layer
        """
        filename = storage.Storage.initialize_table_phys_link(
            tablename=self.tablename, schema=self.schema
        )
        return filename


    def add_row(self,data):
        storage.Storage.add_row_to_table(
        table=self.tablename, phys_link = self.phys_link, data=data
        )
