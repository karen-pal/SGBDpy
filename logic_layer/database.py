import os
import table


import storage_layer
class Database:
    def __init__(self, *, use=True,name):
        self.in_use = use
        self.name = name.lower()
        self.location = storage_layer.storage.Storage.initialize_database(self.name)


    def add_table(self, *, schema=schema, tablename=tablename)
        # pass this task to the storage layer
        if not self.in_use:
            print("can't perfom operations on not-in-use db")
        else:
            new_table = table.Table(schema=schema,tablename=tablename)




os.mkdir("../data/"+self.name)
