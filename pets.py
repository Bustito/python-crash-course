pet_0 = {
    'dueño': 'mirtha legrand',
    'tipo': 'dinosaurio',
    'nombre': 'rexie' 
}

pet_1 = {
    'dueño': 'alberto fernandez de fernandez',
    'tipo': 'perro',
    'nombre': 'dylan'
}

pet_2 = {
    'dueño': 'cristina fernandez',
    'tipo': 'humano',
    'nombre': 'aberto fernandez de fernandez'
}

pets = []

pets.append(pet_0)
pets.append(pet_1)
pets.append(pet_2)

for pet in pets:
    print(f"\n{pet['nombre'].title()}")

    for dato, valor in pet.items():
        if dato != 'nombre':
            print(f"\t{dato.capitalize()}: {valor.title()}")