rivers = {
    'de la plata' : 'argentina',
    'nilo' : 'egipto',
    'rihn' : 'suiza'
}

for river, country in rivers.items():
    print(f"El rio {river.title()} pasa por {country.title()}")
print("\nLos rios que se encuentran en el diccionario rivers son: ")
for river in rivers.keys():
    print(f"\t{river.title()}")
print(f"\nLas cuidades que se encuantran en el diccionario rivers son: ")
for country in rivers.values():
    print(f"\t{country.title()}")