# phys layer stuff
import os
from error import InvalidColumnName

class Storage:

    @staticmethod
    def initialize_database(name):
    if not os.path.exists(name):
        path = "./data/"+name
        os.mkdir(path)
        print("> initialized database. Storage located in ", path)
    else:
        print("Use another database NAME pls")

    @staticmethod
    def initialize_table_file(*,tablename,schema):
        filename = dirname+ "/data/"+ self.tablename + ".stol" #table in croatian
        f = open(filename, "w")
        f.write(str(self.schema))
        f.close()
        return filename

    def add_row(table, data):
        table.file.phys_write(data.format_data(table.schema))


    def add_column(table, column_name, column_type):
        new_table = Table(
            table.name, extend_schema(schema, column_name, column_type), table.file
        )


    def extend_schema(schema, column_name, column_type):
        if column_name not in schema and column_name:
            return schema + (column_name, column_type)
        else:
            raise InvalidColumnName(column_name, schema)
