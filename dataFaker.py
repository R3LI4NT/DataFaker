from banner.banner import *
from faker import Faker
import pandas 
import json
import argparse

def regions():
    banner()
    regiones = {
        	"es_AR": "Argentina",
		"BR": "Brasil",
		"MX": "Mexico",
		"ES": "España",
		"US": "Estados Unidos",
		"CA": "Canada",
		"AU": "Australia",
		"GB": "Gran Bretaña",
		"BG": "Bulgaria",
		"DE": "Alemania",
		"CH": "Republica Checa",
		"GR": "Griego",
		"IR": "Iran",
		"FI": "Finlandia",
		"FR": "Francia",
		"IN": "India",
		"HR": "Croacia",
		"IT": "Italia",
		"JP": "Japon",
		"KR": "Korea",
		"LT": "Lituania",
		"LV": "Letonia",
		"NP": "Nepal",
		"NL": "Paises Bajos/Holanda",
		"NO": "Noruega",
		"PL": "Polonia",
		"PT": "Portugal",
		"RU": "Rusia",
		"SI": "Eslovenia",
		"SE": "Suecia",
		"TR": "Turquia",
		"UA": "Ucrania",
		"CN": "China",
		"TW": "China/Taiwan"
    }
    listaRegiones = json.dumps(regiones, indent=4)
    print("\033[0;31m[+]\033[0m Lista de regiones disponibles:\n", listaRegiones)


def genData():
    banner()
    def generate_random_email():
    	dummy = Faker()
    	return dummy.email()
  
    if parse.region:
        faker = Faker(f'{parse.region}')
        if parse.name:
            names = [faker.unique.name() for i in range(parse.data)]
            print("\n\033[0;31m[+]\033[0m Nombres generados:")
            for i in names:
                print(i)
                data = pandas.DataFrame(names)
                data.columns, data.shape
                data.to_csv('names-fakes')
                
        if parse.address:
            address = [faker.unique.address() for i in range(parse.data)]
            print("\n\033[0;31m[+]\033[0m Direcciones generadas:")
            for i in address:
                print(i)
                data = pandas.DataFrame(address)
                data.columns, data.shape
                data.to_csv('address-fakes')
                
        if parse.jobs:
            empleos = [faker.job() for i in range(parse.data)]
            print("\n\033[0;31m[+]\033[0m Empleos generados:")
            for i in empleos:
                print(i)
                data = pandas.DataFrame(empleos)
                data.columns, data.shape
                data.to_csv('jobs-fakes')
                
        if parse.phone:
            phone_number = [faker.phone_number() for i in range(parse.data)]
            print("\n\033[0;31m[+]\033[0m Numeros telefonicos generados:")
            for i in phone_number:
                print(i)
                data = pandas.DataFrame(phone_number)
                data.columns, data.shape
                data.to_csv('phoneNumber-fakes')
                
        if parse.email:
            email = [generate_random_email()  for i in range(parse.data)]
            print("\n\033[0;31m[+]\033[0m Direcciones de correo generados:")
            for i in email:
                print(i)
                data = pandas.DataFrame(email)
                data.columns, data.shape
                data.to_csv('emails-fakes')
                
        if parse.passport:
            passport = [faker.passport_number()for i in range(parse.data)]
            print("\n\033[0;31m[+]\033[0m Numeros de pasaporte generados:")
            for i in passport:
                print(i)
                data = pandas.DataFrame(passport)
                data.columns, data.shape
                data.to_csv('phoneNumber-fakes')
                
        if parse.url:
            url = [faker.unique.url() for i in range(parse.data)]
            print("\n\033[0;31m[+]\033[0m Direcciones URL generadas:")
            for i in url:
                print(i)
                data = pandas.DataFrame(url)
                data.columns, data.shape
                data.to_csv('urls-fakes')

if __name__ == '__main__':
    try:
        parse = argparse.ArgumentParser()
        parse.add_argument('-l', '--list', help="Lista de regiones disponibles", action='store_true', required=False)
        parse.add_argument('-r', '--region', help="Region", required=False)
        parse.add_argument('-n', '--name', help="Generar nombres falsos", action='store_true', required=False)
        parse.add_argument('-u', '--url', help="Generar URL falsas", action='store_true', required=False)
        parse.add_argument('-a', '--address', help="Generar direcciones falsas", action='store_true', required=False)
        parse.add_argument('-e', '--email', help="Generar direcciones falsas", action='store_true', required=False)
        parse.add_argument('-j', '--jobs', help="Generar empleos de trabajo", action='store_true', required=False)
        parse.add_argument('--phone', help="Generar numeros telefonicos", action='store_true', required=False)
        parse.add_argument('--passport', help="Generar numeros de pasaporte", action='store_true', required=False)
        parse.add_argument('-d', '--data', help="Cantidad de data", type=int, required=False)
        parse = parse.parse_args()
        
        if parse.list:
            regions()
        else:
            genData()
    except KeyboardInterrupt:
        exit()
