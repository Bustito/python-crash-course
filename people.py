people = []

person_0 = {
    'full name' : 'andre stevenson',
    'lives in' : 'pensilvania',
    'age' : 25,
    'profession' : 'electricist'
    }

person_1 = {
    'full name' : 'analia fernandez',
    'lives in' : 'california',
    'age' : 22,
    'profession' : 'accountant'
    }

person_2 = {
    'full name' : 'richard brooke',
    'lives in' : 'pensilvania',
    'age' : 24,
    'profession' : 'shop keeper'
    }

people.append(person_0)
people.append(person_1)
people.append(person_2)

for person in people:
    print(f"\n{person['full name'].title()}")
    for data, value in person.items():

        if data != 'full name':
            print(f"{data.capitalize()} : {str(value).capitalize()}")