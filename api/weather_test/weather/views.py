import os

import requests
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class WeatherDetail(APIView):

    @method_decorator(cache_page(60 * 30))
    def get(self, request: Request, format=None):
        city = request.GET.get("city", None)
        if city != city.lower():
            return redirect(f"/weather?city={city.lower()}")

        if city:
            WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
            GEOCODE_API_KEY = os.getenv("GEOCODE_API_KEY")

            geo_link = f'https://geocode-maps.yandex.ru/1.x?apikey={GEOCODE_API_KEY}&geocode={city}&format=json'
            geo_response = requests.get(geo_link).json()
            geo_cords = geo_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']

            longitude, latitude = geo_cords.split(" ")

            weather_link = f"https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}"
            weather_response = requests.get(weather_link, headers={"X-Yandex-API-Key": WEATHER_API_KEY}).json()

            temperature = weather_response['fact']['temp']
            pressure = weather_response['fact']['pressure_mm']
            wind_speed = weather_response['fact']['wind_speed']

            return Response({"temp": temperature, "pressure": pressure, "wind_speed": wind_speed})

        return Response("Ожидается query параметр city", status=203)

