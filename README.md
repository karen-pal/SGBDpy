# SGDB..py?
<p align="center">
  <img width="500" height="300" src="https://i.imgur.com/Tz35u9v.png" alt="tu nuevo SGDB">
</p>

> WIP

**,,el nuevo SGDB de preferencia""**

## Estado
* construyendo funcionalidades de abajo hacia arriba.
* hasta hay un par de tests

## Instalación

```
git clone https://github.com/karen-pal/SGBDpy.git
cd SGDBpy

virtualenv env
. env/bin/activate
pip install click termcolor
pip install -e .
```

### To run all tests in directory

```
cd tests
python -m unittest discover .
```

### To run single test file

```
cd tests
python -m unittest <test_file>.py
```

## Correr implementación de client layer (WIP)

```
cd client layer
python client.py --create_db=True cosoTest
> initialized database. Storage located in  /my/awesome/path/sgbdpy/storage_layer/data/cosotest
```

## Idea

La idea es que esto a la larga tenga una estructura de plugins.
Es decir, que existan en paralelo distintas implementaciones de la capa física,
de la capa lógica y de la del cliente y que uno pueda "enchufarlas" de una forma
"plug and play".

Para esto se tienen que definir e implementar interfaces a respetar intra-layers!


generate_database
generate_table
add_record
