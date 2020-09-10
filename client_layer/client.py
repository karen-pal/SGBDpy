import click
from termcolor import colored
from logic_layer import database
from logic_layer import table
from client_layer import utils

@click.command()
#@click.option('--use_config_file', default=True, help='Specify options in a config file')
@click.argument('config_file')
def sgbd(config_file):

    print(colored("> WIP sgbd.... BE WARNED","red"))
    use_config_file = True
    if use_config_file:
        content = utils.parse_input(config_file)
        db = database.Database(name = content["database_name"])
        #for elem in content["tables"]:
        #    created_table = table.Table(tablename=elem["tablename"], schema=elem["schema"], db=db.name)
        #    for data in elem["data"]:
        #        created_table.add_row(data)
    print(colored("!!!!! can't believe that worked","green"))
if __name__ == '__main__':
    sgbd()
