import requests
import os
from urllib.parse import urlparse, unquote


def download_picture(picture_url, picture_endpoint):
    unquoted = unquote(picture_url)
    parsed = urlparse(unquoted)
    splited_path = os.path.split(parsed.path)
    filename = splited_path[-1]
    response = requests.get(picture_url)
    response.raise_for_status()
    with open(picture_endpoint+"/"+filename, "wb") as file:
        file.write(response.content)


def get_format_from_link(link):
    unquoted = unquote(link)
    parsed = urlparse(unquoted)
    splited_path = os.path.split(parsed.path)
    splited_tail = os.path.splitext(splited_path[-1])
    return splited_tail[-1]


def fetch_apods_nasa(picture_endpoint,
                     nasa_api_key):
    payload = {
        "api_key": nasa_api_key,
        "count": "50"
    }
    response = requests.get("https://api.nasa.gov/planetary/apod",
                            params=payload)
    response.raise_for_status()

    for apod_features in response.json():
        if apod_features["media_type"] == "image":
            picture_link = apod_features["url"]
            format_from_link = get_format_from_link(picture_link)
            if format_from_link in (".jpg", ".png"):
                download_picture(picture_link, picture_endpoint)


def form_link_on_epic_nasa(image_name, date, nasa_api_key):
    year, month, day = date.split("-")
    return f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png?api_key={nasa_api_key}"


def fetch_epics_nasa(picture_endpoint,
                     nasa_api_key, date_for_epic):
    payload = {
        "api_key": nasa_api_key
    }
    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{date_for_epic}",
                            params=payload)
    response.raise_for_status()
    for epic_features in response.json():
        link_to_epic = form_link_on_epic_nasa(epic_features["image"],
                                              date_for_epic, nasa_api_key)
        download_picture(link_to_epic, picture_endpoint)
