# table_types int(len) || string(len)
import column


class Schema:
    def __init__(self, columns):
        self.raw = ''.join(str(elems) for elems in columns)
        self.columns = self.validated_columns(columns)
    def __str__(self):
        representation = ""
        for single_column in self.columns:
            representation += single_column.column_name + " " + str(single_column.column_type) + ", "
        return representation
    @staticmethod
    def validated_columns(raw_columns):
        """
        get: list of tuples
        output: list of Columns
        """
        columns = []
        for raw_column in raw_columns:
            processed_column = column.Column(raw_column[0], raw_column[1])
            columns.append(processed_column)
        return columns
