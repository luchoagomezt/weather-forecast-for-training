from lib.weather import Weather

CITY = "hamilton,ca"
VALID_WEATHER = ["Rain", "Snow", "Extreme"]


def test_weather_forecast_is_valid():
    weather = Weather(CITY).get_weather_forecast()
    assert weather in VALID_WEATHER


def test_min_temperature_forecast_is_valid():
    min_temperature = Weather(CITY).get_min_temperature()
    assert min_temperature > 200


def test_max_temperature_forecast_is_valid():
    max_temperature = Weather(CITY).get_max_temperature()
    assert max_temperature > 200
