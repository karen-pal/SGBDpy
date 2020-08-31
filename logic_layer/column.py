class Column:
    def __init__(self, column_name, column_type):
        self.column_name = column_name.lower()
        self.column_type = self.parsed(column_type)

    @staticmethod
    def parsed(column_type):
        actual_type = column_type.split("(")[0].lower()
        length = int(column_type.split("(")[1].split(")")[0])
        return (actual_type, length)
