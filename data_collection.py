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
