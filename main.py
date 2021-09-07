from dotenv import load_dotenv
import os
import telegram
import time
from fetch_nasa import fetch_epics_nasa, fetch_apods_nasa
from fetch_spacex import fetch_spacex_launch


def send_imgs_to_tg(astrobot_api_key_tg, astro_chat_id_tg,
                    picture_endpoint):
    bot = telegram.Bot(astrobot_api_key_tg)
    for picture in os.listdir(picture_endpoint):
        bot.send_document(chat_id=astro_chat_id_tg,
                          document=open(f"{picture_endpoint}/{picture}", "rb"))
        time.sleep(86400)


def main():
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    astrobot_api_key_tg = os.getenv("ASTROBOT_API_KEY_TG")
    astro_chat_id_tg = os.getenv("ASTRO_CHAT_ID_TG")

    spacex_launch_number = os.getenv("SPACEX_LAUNCH_NUMBER", "14")
    picture_endpoint = os.getenv("WHERE_TO_PUT_PICTURES",
                                 f"{os.getcwd()}/images")
    date_for_epic = os.getenv("DATE_FOR_EPIC", "2018-08-15")

    fetch_spacex_launch(spacex_launch_number, picture_endpoint)
    fetch_epics_nasa(picture_endpoint,
                     nasa_api_key, date_for_epic)
    fetch_apods_nasa(picture_endpoint, nasa_api_key)
    send_imgs_to_tg(astrobot_api_key_tg, astro_chat_id_tg,
                    picture_endpoint)


if __name__ == "__main__":
    main()
