participants = ['aldous', 'nicolai', 'phil', 'jen', 'samantha']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for participant in participants:
    if participant in favorite_languages.keys():
        print(f"Gracias {participant} por hacer la encuesta")
    else:
        print(f"{participant}, por favor, tome la encuesta")