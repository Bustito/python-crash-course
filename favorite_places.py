favorite_places = {
    'martin': ["alaska's forests", 'europe forests'],
    'juan': ["countryside's"],
    'pilar': ['villa gessell', 'pinamar', 'rio de janeiro']
    }

for persona, lugares in favorite_places.items():
    print(f"\nLos lugares favoritos de {persona.capitalize()} son: ")

    for lugar in lugares:
        print(f"\t{lugar.capitalize()}")