![DataFaker](https://github.com/R3LI4NT/DataFaker/assets/75953873/0c7b8399-13c8-4fad-8d12-6817c1031ca9)

DataFaker es un script que utiliza la librería de <a href="https://faker.readthedocs.io/en/master/">**Faker**</a> para generar información falsa a partir de la región especificada. Es capaz de generar direcciones de correo, números telefónicos, nombres, empleos de trabajos, número de pasaporte, direcciones geográficas, y URLs falsas. 

![regions](https://github.com/R3LI4NT/DataFaker/assets/75953873/c69a4e2c-3652-4da7-b6ac-9bd1a6368c9c)

#### Instalación:

```
> git clone https://github.com/R3LI4NT/DataFaker
> cd DataFaker
> pip3 install -r requirements.txt
> python3 dataFaker.py --help
```

## Uso:
| COMANDO | DESCRIPCION |
| ------------- | ------------- |
| -l/--list | Lista de regiones disponibles  |
| -r/--region  | Region  |
| -d/--data  | Cantidad de data  |
| -n/--name  | Generar nombres falsos  |
| -u/--url  | Generar URL falsas  |
| -a/--address  | Generar direcciones falsas  |
| -e/--email  | Generar direcciones de correo falsos  |
| --phone  | Generar numeros telefonicos falsos  |
| --passport  | Generar numeros de pasaporte falsos  |

`EJEMPLO:` **Generar 10 nombres falsos (Argentina):**

```
python3 dataFaker.py -r es_AR --name -d 10
```

![names](https://github.com/R3LI4NT/DataFaker/assets/75953873/34497972-f9ce-4f41-bdec-b4dbdb977463)

`EJEMPLO:` **Generar direcciones geográficas:**

```
python3 dataFaker.py -r pt_BR --address -d 15
```

![address](https://github.com/R3LI4NT/DataFaker/assets/75953873/a307d8ec-94be-4f3e-800d-f5bbae71a46d)

`EJEMPLO:` **Generar URL:**

```
python3 dataFaker.py -r es_AR --url -d 5
```

![url](https://github.com/R3LI4NT/DataFaker/assets/75953873/8332c7e5-92c5-4856-9e15-9b4a162b659b)

`EJEMPLO:` **Generar números telefónicos:**

```
python3 dataFaker.py -r es_AR --phone -d 10
```

![phone](https://github.com/R3LI4NT/DataFaker/assets/75953873/babcc5a9-e9d6-417c-b3d8-c7372a43da70)

`EJEMPLO:` **Generar empleos de trabajo:**

```
python3 dataFaker.py -r es_AR --jobs -d 5
```

![jobs](https://github.com/R3LI4NT/DataFaker/assets/75953873/d9da9a80-668f-42b7-af50-e72b9da29389)

`EJEMPLO:` **Generar direcciones de correo falsos:**

```
python3 dataFaker.py -r es_AR --email -d 5
```

![email](https://github.com/R3LI4NT/DataFaker/assets/75953873/90aee0bb-7509-4619-bc58-00433f342438)

`EJEMPLO:` **Generar números de pasaporte falsos:**

```
python3 dataFaker.py -r es_AR --passport -d 10
```

![passport](https://github.com/R3LI4NT/DataFaker/assets/75953873/cdc91531-aef8-43f3-bbc9-e252ed3abdcd)



No me hago responsable del mal uso que se le pueda dar a esta herramienta, úselo con fines educativos.
