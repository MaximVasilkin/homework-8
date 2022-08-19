import requests


# Задача-1.

def smarter_hero(list_heroes_names,
                 url='https://akabab.github.io/superhero-api/api/',
                 parameter='/all.json'):
    all_characters = requests.get(url + parameter).json()
    characters_info = {}
    for character_dict in all_characters:
        if character_dict['name'] in list_heroes_names:
            characters_info[character_dict['name']] = \
                character_dict['powerstats']['intelligence']
    return max(characters_info, key=characters_info.get)


if __name__ == '__main__':
    print(smarter_hero(['Hulk', 'Captain America', 'Thanos'],))

# Задача-2.

