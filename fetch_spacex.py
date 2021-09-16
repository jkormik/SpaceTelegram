import requests
from aiding_functions import download_picture, get_format_from_link


def fetch_spacex_launch(spacex_launch_number, picture_endpoint):
    response = requests.get(f"https://api.spacexdata.com/v3/launches/{spacex_launch_number}")
    response.raise_for_status()
    links_to_spacex_imgs = response.json()["links"]["flickr_images"]
    for link in links_to_spacex_imgs:
        format_from_link = get_format_from_link(link)
        if format_from_link in (".jpg", ".png"):
            download_picture(link, picture_endpoint)
