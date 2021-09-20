import os
from urllib.parse import urlparse, unquote
import requests


def download_picture(picture_url, picture_path, **params):
    unquoted = unquote(picture_url)
    parsed = urlparse(unquoted)
    splited_path = os.path.split(parsed.path)
    filename = splited_path[-1]
    response = requests.get(picture_url, params=params)
    response.raise_for_status()
    with open(f"{picture_path}/{filename}", "wb") as file:
        file.write(response.content)


def get_file_format_from_link(link):
    unquoted = unquote(link)
    parsed = urlparse(unquoted)
    splited_parsed_path = os.path.splitext(parsed.path)
    return splited_parsed_path[-1]
