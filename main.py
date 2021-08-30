from dotenv import load_dotenv
import os
import telegram
import time
from fetch_nasa import fetch_epics_nasa, fetch_apods_nasa
from fetch_spacex import fetch_spacex_launch


def send_imgs_to_tg(astrobot_api_key_tg, astro_chat_id_tg,
                    picture_endpoint, period_of_sending):
    bot = telegram.Bot(astrobot_api_key_tg)
    for picture in os.listdir(picture_endpoint):
        time.sleep(int(period_of_sending))
        bot.send_document(chat_id=astro_chat_id_tg,
                          document=open(f"{picture_endpoint}/{picture}", "rb"))


def main():
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    picture_endpoint = os.getenv("WHERE_TO_PUT_PICTURES")
    spacex_launch_url = os.getenv("LINK_TO_SPACEX_LAUNCH")
    apod_nasa_link = os.getenv("LINK_TO_APOD_NASA")
    epic_nasa_link = os.getenv("LINK_TO_EPIC_NASA")
    how_much_apods_try_to_download = os.getenv("HOW_MUCH_APODS_TRY_TO_DOWNLOAD")
    date_for_epic = os.getenv("DATE_FOR_EPIC")
    astrobot_api_key_tg = os.getenv("ASTROBOT_API_KEY_TG")
    astro_chat_id_tg = os.getenv("ASTRO_CHAT_ID_TG")
    period_of_sending = os.getenv("PERIOD_OF_SENDING_TO_TG")

    fetch_epics_nasa(epic_nasa_link, picture_endpoint,
                     nasa_api_key, date_for_epic)
    fetch_apods_nasa(apod_nasa_link, picture_endpoint, nasa_api_key,
                     how_much_apods_try_to_download)
    fetch_spacex_launch(spacex_launch_url, picture_endpoint)
    send_imgs_to_tg(astrobot_api_key_tg, astro_chat_id_tg,
                    picture_endpoint, period_of_sending)


if __name__ == "__main__":
    main()
