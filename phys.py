# phys layer stuff

from error import InvalidColumnName


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
