# DataFaker

DataFaker es un script que utiliza la librería de <a href="https://faker.readthedocs.io/en/master/">**Faker**</a> para generar información falsa a partir de la región especificada.

<p align="center">
   <img src="https://raw.githubusercontent.com/R3LI4NT/DataFaker/main/img/regions.png">
</p>

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
| -e/--email  | Generar direcciones de correo falsas  |
| --phone  | Generar numeros telefonicos falsos  |
| --passport  | Generar numeros de pasaporte falsos  |

`EJEMPLO:` **Generar 10 nombres falsos (Argentina): **
```
python3 dataFaker.py -r es_AR --name -d 10
```

![names](https://github.com/R3LI4NT/DataFaker/assets/75953873/34497972-f9ce-4f41-bdec-b4dbdb977463)
