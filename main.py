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

import os


class YaDisk():
    def __init__(self, token):
        self.token = token

    def uplaod_file(self, path_from, path_to=''):
        with open(path_from, encoding='utf-8') as file:
            file_name = os.path.basename(file.name)
        self.path_from = path_from
        self.path_to = f'{path_to}/{file_name}'
        self._url = r'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self._params = {'path': self.path_to, 'overwrite': 'true'}
        self._headers = {'Content-Type': 'application/json',
                         'Authorization': f'OAuth {self.token}'}
        self.check_meta = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                  params={'path': '/'},
                                  headers=self._headers)
        self.list_names = []
        for item in self.check_meta.json()['_embedded']['items']:
            self.list_names.append(item['name'])
        if path_to and path_to not in self.list_names:
            self.create_folder = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                         params={'path': f'/{path_to}'},
                         headers=self._headers)
            print(self.create_folder)
            self.link = requests.get(self._url,
                                     params=self._params,
                                     headers=self._headers).json().get('href', None)
            print(requests.put(self.link, data=open(path_from, 'rb')))
        else:
            self.link = requests.get(self._url,
                                     params=self._params,
                                     headers=self._headers).json().get('href', None)
            print(requests.put(self.link, data=open(path_from, 'rb')))

    def delete_file(self, path, permanently='false'):
        self.path = path
        self._url = r'https://cloud-api.yandex.net/v1/disk/resources'
        self._params = {'path': self.path, 'permanently': permanently}
        self._headers = {'Content-Type': 'application/json',
                         'Authorization': f'OAuth {self.token}'}
        print(requests.delete(self._url, params=self._params, headers=self._headers))



if __name__ == '__main__':
    disk = YaDisk('token')
    disk.uplaod_file('тестовый документ (1).txt', 'Новая папка')
#   disk.delete_file('тестовый документ (1).txt', 'Новая папка')








