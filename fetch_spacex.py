import requests
import pathlib
import os
from urllib.parse import urlparse, unquote


def download_picture(picture_url, picture_endpoint):
    format_from_link = get_format_from_link(picture_url)
    if format_from_link == ".jpg" or format_from_link == ".png":
        unquoted = unquote(picture_url)
        parsed = urlparse(unquoted)
        splited_path = os.path.split(parsed.path)
        filename = splited_path[-1]
        response = requests.get(picture_url)
        response.raise_for_status()
        pathlib.Path(picture_endpoint).mkdir(exist_ok=True)
        with open(picture_endpoint+"/"+filename, "wb") as file:
            file.write(response.content)


def fetch_spacex_launch(spacex_launch_url, picture_endpoint):
    response = requests.get(spacex_launch_url)
    response.raise_for_status()
    links_to_spacex_imgs = response.json()["links"]["flickr_images"]
    for link in links_to_spacex_imgs:
        download_picture(link, picture_endpoint)


def get_format_from_link(link):
    unquoted = unquote(link)
    parsed = urlparse(unquoted)
    splited_path = os.path.split(parsed.path)
    splited_tail = os.path.splitext(splited_path[-1])
    return splited_tail[-1]
