import requests
from pprint import pprint
from Token import token


class YaUploader:
    URL_FILES_LIST: str = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    URL_UPLOAD_LiNK: str = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token
        print(self.token)

    @property
    def header(self):
        return {'Accept': 'application/json', 'Authorization': f"OAuth{self.token}"}

    def get_files_list(self):
        print(self.header)
        responce = requests.get(self.URL_FILES_LIST, headers=self.header)
        pprint(responce.json())


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя


    uploader = YaUploader(token)
    result = uploader.get_files_list()