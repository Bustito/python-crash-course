favorite_numbers = {
    'mike': [3, 9, 22],
    'steven': [5, 87, 1],
    'andrea': [999, 0],
    'samantha': [25, 9],
    'kevin': [14]
}

for person, numbers in favorite_numbers.items():
    if len(numbers) != 1:   #Identifico aquellos con un solo numero favorito
        string = ', '.join(map(str, numbers))   #Quito el formato de lista []
        print(f"Los numeros favoritos de {person} son: {string}")
    else:
        print(f"El numero favorito de {person} es {numbers[0]}")