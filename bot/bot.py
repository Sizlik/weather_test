import os

import requests
from telebot import TeleBot

GET_WEATHER_ENDPOINT = os.getenv("GET_WEATHER_ENDPOINT")
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = TeleBot(TOKEN)


@bot.message_handler(func=lambda m: True)
def get_weather(message):
    response = requests.get(f"{GET_WEATHER_ENDPOINT}?city={message.text}").json()

    message_to_send = f"""Погодные данные в городе {message.text}:

Температура: {response['temp']}
Атмосферное давление: {response['pressure']} мм рт. ст.
Скорость ветра: {response['wind_speed']} м/с"""

    bot.send_message(message.from_user.id, message_to_send)


bot.polling(none_stop=True, non_stop=True)
