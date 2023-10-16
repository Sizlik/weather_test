from django.urls import include, path
from rest_framework import routers
from weather_test.weather.views import WeatherDetail

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('weather/', WeatherDetail.as_view())
]
