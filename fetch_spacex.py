import requests
from link_processing import get_file_format_from_link
from data_collection import download_picture


def fetch_spacex_launch(spacex_launch_number, picture_path):
    response = requests.get(f"https://api.spacexdata.com/v3/launches/{spacex_launch_number}")
    response.raise_for_status()
    spacex_img_links = response.json()["links"]["flickr_images"]
    for link in spacex_img_links:
        file_format_from_link = get_file_format_from_link(link)
        if file_format_from_link in (".jpg", ".png"):
            download_picture(link, picture_path)
