from dotenv import load_dotenv
import os
import telegram
import time
from fetch_nasa import fetch_nasa_epics, fetch_nasa_apods
from fetch_spacex import fetch_spacex_launch
import pathlib


def send_imgs_to_tg(telegram_bot_api_key, telegram_chat_id,
                    picture_path):
    bot = telegram.Bot(telegram_bot_api_key)
    for picture in os.listdir(picture_path):
        with open(f"{picture_path}/{picture}", "rb") as document:
            bot.send_document(chat_id=telegram_chat_id,
                              document=document)
        time.sleep(86400)


def main():
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    telegram_bot_api_key = os.getenv("TELEGRAM_BOT_API_KEY")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    spacex_launch_number = os.getenv("SPACEX_LAUNCH_NUMBER", "14")
    picture_path = os.getenv("WHERE_TO_PUT_PICTURES",
                                 f"{os.getcwd()}/images")
    date_for_epic = os.getenv("DATE_FOR_EPIC", "2018-08-15")

    pathlib.Path(picture_path).mkdir(exist_ok=True)

    fetch_spacex_launch(spacex_launch_number, picture_path)
    fetch_nasa_epics(picture_path,
                     nasa_api_key, date_for_epic)
    fetch_nasa_apods(picture_path, nasa_api_key)
    send_imgs_to_tg(telegram_bot_api_key, telegram_chat_id,
                    picture_path)


if __name__ == "__main__":
    main()
