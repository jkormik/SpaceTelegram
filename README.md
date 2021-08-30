# Space Telegram

The script is collecting images of rocket launches and space via SpaceX and Nasa API and posting them to a Telegram Channel of chose via a Telegram Bot of chose.

### How to install

First of all you'll need to get **NASA API Key**, *Telegram Bot HTTP API Access Token* and **Telegram Group Chat ID**.

You can get **Nasa API Key** [here](https://api.nasa.gov/).
**NASA API Key** looks something like this `123ljjlj1khj14j1h2lk3k23jkjJLKJL2j334534`.
**NASA API Key** should be assigned to `NASA_API_KEY` in `.env`.

You can get *Telegram Bot HTTP API Access Token* via [BotFather in Telegram](https://telegram.im/BotFather).
*Telegram Bot HTTP API Access Token* looks something like this `7734627368:TTTT7gHGG878d87987Dhgh7687_6ghjghgj`.
*Telegram Bot HTTP API Access Token* should be assigned to `ASTROBOT_API_KEY_TG` in `.env`.

[This link](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id) will help you to get **Telegram Group Chat ID** after you've created a bot, a group and added bot to a group as any other member.
**Telegram Group Chat ID** looks something like this `-7859788435839`.
**Telegram Group Chat ID** should be assigned to `ASTRO_CHAT_ID_TG` in `.env`.

In `.env` you should also configure:

* *Endpoint path of downloaded via API pictures.* This value should be assigned to `WHERE_TO_PUT_PICTURES ` in `.env` and looks something like this - 'F:/Barneby/Desktop/images' (string);
* *Link to SpaceX launch of chose.* This value should be assigned to `LINK_TO_SPACEX_LAUNCH` in `.env` and looks something like this - `https://api.spacexdata.com/v3/launches/14` (string);
* *Link to Astronamy Picture of the Day (APOD).* This value should be assigned to `LINK_TO_APOD_NASA` in `.env` and looks something like this - `https://api.nasa.gov/planetary/apod` (string);
* *How much Astronomy Pictures of the Day (APODs) you want to try to download.* This value should be assigned to `HOW_MUCH_APODS_TRY_TO_DOWNLOAD` in `.env` and looks something like this - `15` (integer);
* *Link to Earth Polychromatic Imaging Camera (EPIC).* This value should be assigned to `LINK_TO_EPIC_NASA` in `.env` and looks something like this - `https://api.nasa.gov/EPIC/api/natural/date` (string);
* *The date on which natural color imagery (EPIC) was made.* This value should be assigned to `DATE_FOR_EPIC` in `.env` and looks something like this - `2018-08-15` (string in given format);
* *Period in which downloaded picture will be posted via the Bot to the Group Chat in seconds.* This value should be assigned to `PERIOD_OF_SENDING_TO_TG` in `.env` and looks something like this - `86400` (integer).

Example of completed `.env` file.

```
WHERE_TO_PUT_PICTURES="F:/Barneby/Desktop/images"
LINK_TO_SPACEX_LAUNCH="https://api.spacexdata.com/v3/launches/14"
NASA_API_KEY="123ljjlj1khj14j1h2lk3k23jkjJLKJL2j334534"
LINK_TO_APOD_NASA="https://api.nasa.gov/planetary/apod"
HOW_MUCH_APODS_TRY_TO_DOWNLOAD=15
LINK_TO_EPIC_NASA="https://api.nasa.gov/EPIC/api/natural/date"
DATE_FOR_EPIC="2018-08-15"
ASTROBOT_API_KEY_TG="7734627368:TTTT7gHGG878d87987Dhgh7687_6ghjghgj"
ASTRO_CHAT_ID_TG="-7859788435839"
PERIOD_OF_SENDING_TO_TG=86400
```

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).