# phys layer stuff
from termcolor import colored
import os
from error import InvalidColumnName

FILE = "file"

dirname = os.path.dirname(__file__)

class Storage:

    def __init__(self):
        self.phys_link = FILE
        self.db_in_use = None
        self.db_path = None
        self.created_tables = []

    @classmethod
    def initialize_database(cls,name):
        print("Initializing database...")
        if not os.path.exists(name):
            path = dirname+"/data/" + name
            os.mkdir(path)
            print(colored(f"> initialized database. Storage located in {path}","green"))
            cls.db_path = path
            cls.db_in_use = name
        else:
            print("Use another database NAME pls")

    def initialize_table_phys_link(self,*, tablename, schema):
        print("###########")
        #print(dir(cls))
        if not self.db_path:
            print(colored("No db configured as in use","red"))
            return
        for elem in self.created_tables:
            if tablename in elem.values():
                print(colored(f"table {tablename} already exists","red"))
                return

        filename = self.db_path + tablename + ".stol"  # table in croatian
        f = open(filename, "w")
        f.write(str(schema))
        f.close()
        self.created_tables.append({"tablename":tablename,"file":filename})
        print("> initialized table ", tablename)
        return filename

    @staticmethod
    def add_row_to_table(*,table, data, phys_link):
        f = open(phys_link,"a")
        for elem in data:
            f.write(elem)
        f.close()
        print(f">wrote data in {table}")

    # def add_column(table, column_name, column_type):
    #    new_table = Table(
    #        table.name, extend_schema(schema, column_name, column_type), table.file
    #    )

    @staticmethod
    def extend_schema(schema, column_name, column_type):
        if column_name not in schema and column_name:
            return schema + (column_name, column_type)
        else:
            raise InvalidColumnName(column_name, schema)
