import os
from . import table

from storage_layer import storage

class Database:
    def __init__(self, *, use=True,name):
        self.in_use = use
        self.name = name.lower()
        self.location = storage.Storage.initialize_database(self.name)


    #def add_table(self, *, table_schema=schema, tablename=tablename):
    #    # pass this task to the storage layer
    #    if not self.in_use:
    #        print("can't perfom operations on not-in-use db")
    #    else:
    #        new_table = table.Table(table_schema=schema,tablename=tablename)
