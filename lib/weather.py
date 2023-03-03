import requests
API_ID = "55f5ab2e144704e42c8bf3522249b921"
API_END_POINT = "https://api.openweathermap.org/data/2.5/weather?q=<city>,ca&appid=<api id>"


class Weather:
    def __init__(self, city):
        self.city = city

    def get_weather_forecast(self) -> str:
        response = requests.get(API_END_POINT.replace("<city>", self.city).replace("<api id>", API_ID))
        assert response.status_code == 200
        return response.json()["weather"]

    def get_visibility(self) -> int:
        response = requests.get(API_END_POINT.replace("<city>", self.city).replace("<api id>", API_ID))
        assert response.status_code == 200
        return response.json()["visibility"]

    def get_max_temperature(self) -> int:
        response = requests.get(API_END_POINT.replace("<city>", self.city).replace("<api id>", API_ID))
        assert response.status_code == 200
        return response.json()["main"]["temp_max"] - 273.15

    def get_min_temperature(self) -> int:
        response = requests.get(API_END_POINT.replace("<city>", self.city).replace("<api id>", API_ID))
        assert response.status_code == 200
        return response.json()["main"]["temp_min"] - 273.15
