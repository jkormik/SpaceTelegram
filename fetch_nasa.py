import requests
from aiding_functions import download_picture, get_file_format_from_link


def fetch_nasa_apods(picture_path,
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
            file_format_from_link = get_file_format_from_link(picture_link)
            if file_format_from_link in (".jpg", ".png"):
                download_picture(picture_link, picture_path)


def form_nasa_epic_link(image_name, date):
    year, month, day = date.split("-")
    return f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png"


def fetch_nasa_epics(picture_path,
                     nasa_api_key, date_for_epic):
    payload = {
        "api_key": nasa_api_key
    }
    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{date_for_epic}",
                            params=payload)
    response.raise_for_status()
    for epic_features in response.json():
        link_to_epic = form_nasa_epic_link(epic_features["image"],
                                              date_for_epic)
        download_picture(link_to_epic, picture_path, api_key=nasa_api_key)
