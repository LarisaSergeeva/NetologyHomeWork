import requests
from TOKEN import token


class YaUploader:
    def __init__(self, _token: str):
        self.token = "OAuth " + _token

    def upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        filename = file_path.split('/', )[-1]
        headers = {'Accept': 'application/json', 'Authorization': self.token}
        params = {'path': filename, 'overwrite': 'true'}
        responce = requests.get(upload_url, headers=headers, params=params)
        try:
            responce.raise_for_status()
            print('Соединение установлено.')
        except Exception as e:
            print('Ошибка при загрузке страницы: ' + str(e))
        upload_url_ = responce.json().get("href", "")
        with open(file_path, 'rb') as file:
            responce_ = requests.put(upload_url_, data=file)
        try:
            responce_.raise_for_status()
            print('Соединение установлено.')
        except Exception as e:
            print('Ошибка при загрузке страницы: ' + str(e))
        return "Файл успешно загружен."


if __name__ == '__main__':
    path_to_file = "1.txt"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
