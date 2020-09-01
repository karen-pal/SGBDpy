import click
from termcolor import colored
from logic_layer import database

@click.command()
@click.option('--create_db',default=False, help='Create database with <db_name> name')
#@click.option('--use_db',default=False, help='Create database with <db_name> name')
@click.argument('database_name')
def database_creation(create_db,database_name):
    print(colored("WIP sgbd CLI.... BE WARNED","red"))
    if create_db:
        dir(database)
        database.Database(name = database_name)


if __name__ == '__main__':
    database_creation()
