cities = {
    'barcelona': {
        'pais': 'españa',
        'poblacion': 2845941,
        'fact': 'no todos sus habitantes son del barcelona futbol club'
        },
    'rosario': {
        'pais': 'republica de peronistan',
        'poblacion': 2001234,
        'fact': 'sus lineas de bus son horrendas'
        },
    'buenos aires': {
        'pais': 'chetoslovaquia',
        'poblacion': 'mucha',
        'fact': "la buenos aires 'buena'"
        }
    }

for city, info in cities.items():
    print(f"\n{city.title()}")
    for data, value in info.items():
        print(f"\t{data.capitalize()}: {str(value).capitalize()}")