import KeyParser
import requests
import datetime
import time
import os

class CurrentWeatherData:

    def __init__(self):
        key_file = KeyParser.OpenWeatherMap()
        self.key = key_file.getKey()
        self.name = key_file.getName()
        self.lat = key_file.getLatitude()
        self.lon = key_file.getLongitude()

        self.data = self.getWeatherData()

    def getWeatherData(self):
        http_request = 'http://api.openweathermap.org/data/2.5/weather?q=' + self.name + '&APPID=' + self.key + '&units=imperial'
        
        res = requests.get(http_request)
        return res.json()

    def getLatitude(self):
        return self.data['coord']['lat']

    def getLongitude(self):
        return self.data['coord']['lon']

    def getCoordinates(self):
        lat = self.getLatitude()
        lon = self.getLongitude()
        return [lat, lon]

    def getWeatherId(self):
        return self.data['weather'][0]['id']

    def getWeatherMain(self):
        return self.data['weather'][0]['main']

    def getWeatherDescription(self):
        return self.data['weather'][0]['description']

    def getWeatherIcon(self):
        return self.data['weather'][0]['icon']

    def getBase(self):
        return self.data['base']

    def getMainTemperature(self):
        return self.data['main']['temp']

    def getMainPressure(self):
        return self.data['main']['pressure']  # hPa

    def getMainHumidity(self):
        return self.data['main']['humidity']

    def getMainTemperatureMinimal(self):
        return self.data['main']['temp_min']

    def getMainTemperatureMaximal(self):
        return self.data['main']['temp_max']

    def getVisibility(self):
        return self.data['visibility'] / 1609.344  # MI

    def getWindSpeed(self):
        return self.data['wind']['speed']

    def getWindGust(self):
        try:
            return self.data['wind']['gust']
        except:
            return None

    def getWindBearing(self):            
        try:
            return self.data['wind']['deg']
        except:
            return None

    def getCloudsAll(self):
        return self.data['clouds']['all']

    def getDate(self):
        return datetime.datetime.fromtimestamp(self.data['dt'])

    def getSystemType(self):
        return self.data['sys']['type']

    def getSystemId(self):
        return self.data['sys']['id']

    def getSystemCountry(self):
        return self.data['sys']['country']

    def getSystemSunrise(self):
        return time.ctime(self.data['sys']['sunrise'])

    def getSystemSunset(self):
        return time.ctime(self.data['sys']['sunset'])

    def getTimezone(self):
        return self.data['timezone']

    def getId(self):
        return self.data['id']

    def getName(self):
        return self.data['name']

    def getCod(self):
        return self.data['cod']

    def getRain1H(self):            
        try:
            return self.data['rain']['1h']
        except:
            return None

    def getRain3H(self):            
        try:
            return self.data['rain']['3h']
        except:
            return None

    def getSnow1H(self):            
        try:
            return self.data['snow']['1h']
        except:
            return None

    def getSnow3H(self):            
        try:
            return self.data['snow']['3h']
        except:
            return None

    def printCurrentWeatherData(self):
        print('Currently weather data:\n' \
              'Coordinates: {}\n' \
              'Weather Id: {}\n' \
              'Weather Main: {}\n' \
              'Weather Description: {}\n' \
              'Weather Icon: {}\n' \
              'Base: {}\n' \
              'Main Temperature: {}\n' \
              'Main Pressure: {}\n' \
              'Main Humidity: {}\n' \
              'Main Min. Temperature: {}\n' \
              'Main Max. Temperature: {}\n' \
              'Visibility: {}\n' \
              'Wind Speed: {}\n' \
              'Wind Gust: {}\n' \
              'Wind Bearing: {}\n' \
              'Cloud All: {}\n' \
              'Date: {}\n' \
              'System Type: {}\n' \
              'System Id: {}\n' \
              'System Country: {}\n' \
              'System Sunrise: {}\n' \
              'System Sunset: {}\n' \
              'Timezone: {}\n' \
              'Id: {}\n' \
              'Name: {}\n' \
              'Cod: {}\n' \
              'Rain 1H: {}\n' \
              'Rain 3H: {}\n' \
              'Snow 1H: {}\n' \
              'Snow 3H: {}\n'
              .format(self.getCoordinates(),
                      self.getWeatherId(),
                      self.getWeatherMain(),
                      self.getWeatherDescription(),
                      self.getWeatherIcon(),
                      self.getBase(),
                      self.getMainTemperature(),
                      self.getMainPressure(),
                      self.getMainHumidity(),
                      self.getMainTemperatureMinimal(),
                      self.getMainTemperatureMaximal(),
                      self.getVisibility(),
                      self.getWindSpeed(),
                      self.getWindGust(),
                      self.getWindBearing(),
                      self.getCloudsAll(),
                      self.getDate(),
                      self.getSystemType(),
                      self.getSystemId(),
                      self.getSystemCountry(),
                      self.getSystemSunrise(),
                      self.getSystemSunset(),
                      self.getTimezone(),
                      self.getId(),
                      self.getName(),
                      self.getCod(),
                      self.getRain1H(),
                      self.getRain3H(),
                      self.getSnow1H(),
                      self.getSnow3H()
                  )
              )

    def printCurrentWeatherReport(self):
        print('Weather in {}, {}'.format(self.getName(),
                                         self.getSystemCountry()
                                         )
              )
        print('{} °F\n{}\n{}'.format(self.getMainTemperature(),
                                     self.getWeatherDescription(),
                                     self.getDate()
                                     )
              )
        print('Wind: {} m/h, Direction: {}°, Gust: {}'.format(
                self.getWindSpeed(),
                self.getWindBearing(),
                self.getWindGust()
                )
              )
        print('Cloudiness: {}%'.format(self.getCloudsAll()))
        print('Pressure: {} hpa'.format(self.getMainPressure()))
        print('Humidity: {}%'.format(self.getMainHumidity()))
        print('Rain: {} mm'.format(self.getRain1H()))
        print('Snow: {} mm'.format(self.getSnow1H()))
        print('Visibility: {:.2f} mi'.format(self.getVisibility()))
        print('Sunrise: {}'.format(self.getSystemSunrise()))
        print('Sunset: {}'.format(self.getSystemSunset()))
        print('Geo coordinates: {}'.format(self.getCoordinates()))
        print()
##        print(self.__str__())
##        print()
        

    def saveCurrentWeatherData(self):
        directory = 'data'
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        filename = 'forecast_request' + '-' + time.strftime("%Y%m%d") + '-' + time.strftime("%H%M%S") + '.json'
        with open(os.path.join(directory, filename), 'w') as write_data:
            write_data.write(str(self.data))
            
    def __str__(self):
        return 'Current Weather Data = {}'.format(self.data)
