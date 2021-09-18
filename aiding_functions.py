import os
from urllib.parse import urlparse, unquote
import requests


def download_picture(picture_url, picture_endpoint, **kwargs):
    unquoted = unquote(picture_url)
    parsed = urlparse(unquoted)
    splited_path = os.path.split(parsed.path)
    filename = splited_path[-1]
    response = requests.get(picture_url, params=kwargs)
    response.raise_for_status()
    with open(picture_endpoint+"/"+filename, "wb") as file:
        file.write(response.content)


def get_format_from_link(link):
    unquoted = unquote(link)
    parsed = urlparse(unquoted)
    splited_path = os.path.split(parsed.path)
    splited_tail = os.path.splitext(splited_path[-1])
    return splited_tail[-1]
