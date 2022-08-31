from os import makedirs
from os.path import join
from os.path import split
from os.path import splitext

from urllib.parse import urlsplit

import requests


def download_file_from_url(url, dirname, filename):    
    response = requests.get(url)
    response.raise_for_status()
    
    makedirs(dirname, exist_ok=True)    
    path = join(dirname, filename)

    with open(path, 'wb') as file:
        file.write(response.content)        


def get_json_from_api_request(url, headers=None, params=None):    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def extract_file_ext(url):
    path_dir, file_name = split(
        urlsplit(url).path
    )
    file_name, file_ext = splitext(file_name)
    return file_ext