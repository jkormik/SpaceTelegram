# Space Telegram

The script is collecting images of rocket launches and space via SpaceX and Nasa API and posting them to a Telegram Channel of chose via a Telegram Bot of chose.

### How to install

First of all you'll need to get **NASA API Key**, *Telegram Bot HTTP API Access Token* and **Telegram Group Chat ID**.

You can get **Nasa API Key** [here](https://api.nasa.gov/).
**NASA API Key** looks something like this `123ljjlj1khj14j1h2lk3k23jkjJLKJL2j334534`.
**NASA API Key** should be assigned to `NASA_API_KEY` in `.env`.

You can get *Telegram Bot HTTP API Access Token* via [BotFather in Telegram](https://telegram.im/BotFather).
*Telegram Bot HTTP API Access Token* looks something like this `7734627368:TTTT7gHGG878d87987Dhgh7687_6ghjghgj`.
*Telegram Bot HTTP API Access Token* should be assigned to `TELEGRAM_BOT_API_KEY` in `.env`.

[This link](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id) will help you to get **Telegram Group Chat ID** after you've created a bot, a group and added bot to a group as any other member.
**Telegram Group Chat ID** looks something like this `-7859788435839`.
**Telegram Group Chat ID** should be assigned to `TELEGRAM_CHAT_ID` in `.env`.

In `.env` you may configure:

* *A path to downloaded via API pictures.* This value should be assigned to `WHERE_TO_PUT_PICTURES ` in `.env` and looks something like this - 'F:/Barneby/Desktop/images' (string). By default pictures are downloaded to the directory where `main.py` file is;
* *A number of SpaceX launch of chose.* This value should be assigned to `LINK_TO_SPACEX_LAUNCH` in `.env` and looks something like this - `14` (string). By default it is 14th launch;
* *A date on which natural color imagery (EPIC) was made.* This value should be assigned to `DATE_FOR_EPIC` in `.env` and looks something like this - `2018-08-15` (string in given format). By default it is 2018-08-15.

Example of completed `.env` file.

```
NASA_API_KEY="123ljjlj1khj14j1h2lk3k23jkjJLKJL2j334534"
TELEGRAM_BOT_API_KEY="7734627368:TTTT7gHGG878d87987Dhgh7687_6ghjghgj"
TELEGRAM_CHAT_ID="-7859788435839"
```

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

```
python main.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).