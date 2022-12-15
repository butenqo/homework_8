import requests

most_intelligence = {}
class Hero:
    
    base_url = 'https://akabab.github.io/superhero-api/api/'

    def __init__(self, id):
        self.id = id

    def intelligence(self):
        url = self.base_url + f'id/{self.id}.json'
        response = requests.get(url)
        most_intelligence[response.json()['name']] = response.json()['powerstats']['intelligence']
       
hulk = Hero(332)
captain_america = Hero(149)
thanos = Hero(655)

hulk.intelligence()
captain_america.intelligence()
thanos.intelligence()

print(f'Самый умный: {max(most_intelligence, key=most_intelligence.get)}')


class Yandex:

    base_url = 'https://cloud-api.yandex.net:443'

    def __init__(self, token):
        self.token = token

    def get_upload_link(self, path):
        url = '/v1/disk/resources/upload'
        headers = {'Authorization': f'OAuth {token}'}
        params = {'path': path, 'overwrite': True}
        request_url = self.base_url + url
        response = requests.get(request_url, headers=headers, params=params)
        return response.json()['href']

    def upload_file(self, local_path):
        upload_url = self.get_upload_link(local_path.rpartition("\\")[2])
        headers = {'Authorization': f'OAuth {token}'}
        response = requests.put(upload_url, data = open(local_path, 'rb'), headers=headers)
   
token = 
path_to_file = 
ya = Yandex(token)
ya.upload_file(path_to_file)
