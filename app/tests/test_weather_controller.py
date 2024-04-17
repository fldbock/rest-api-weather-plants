from app.models.plant import Plant
from app.controllers.weather_controller import WeatherController

class TestWeatherController:
    # Read
    def test_read(self, mocked_weather_api_app):
        with mocked_weather_api_app.app_context():            
            weather_controller = WeatherController()            
            weather = weather_controller.read(1, "2024-04-15T02:00")[0]
            
            assert weather['temperature'] == 6.6 and weather['humidity'] == 78 
