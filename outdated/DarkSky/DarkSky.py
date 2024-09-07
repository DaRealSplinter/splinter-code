import KeyParser
import requests
import datetime
import time
import os

class ForecastRequest:
    '''
        A Forecast Request returns the current weather conditions,
        a minute-by-minute forecast for the next hour (where available),
        an hour-by-hour forecast for the next 48 hours, and
        a day-by-day forecast for the next week.

        Plan Type: Trial
        Your trial account allows up to 1,000 free calls per day to evaluate
        the Dark Sky API.
    '''

    def __init__(self):
        key_file = KeyParser.DarkSky()
        self.key = key_file.getKey()
        self.lat = key_file.getLatitude()
        self.lon = key_file.getLongitude()

        # Proxies for the get forecast requests 
        self.proxies = key_file.getProxies()
        
        self.data = self.getForecastRequest()

    def getForecastRequest(self):
        
        # currently, minutely, hourly, daily, alerts, flags
        # res = requests.get('https://api.darksky.net/forecast/' + self.key + '/' + self.lat + ',' + self.lon + '?exclude=minutely,hourly,daily', proxies=proxies)
        # print("Proxies: {}".format(self.proxies))
        if self.proxies == None:
            res = requests.get('https://api.darksky.net/forecast/' + self.key + '/' + self.lat + ',' + self.lon)
        else:
            res = requests.get('https://api.darksky.net/forecast/' + self.key + '/' + self.lat + ',' + self.lon, proxies=self.proxies)
        return res.json()

    ''' Location of the forecast request '''
    def getLatitude(self):
        return self.data['latitude']

    def getLongitude(self):
        return self.data['longitude']

    def getCoordinates(self):
        return [self.data['latitude'], self.data['longitude']]

    def getTimezone(self):
        return self.data['timezone']

    def getOffset(self):
        return self.data['offset']

    ''' Currently data request '''
    def getCurrentlyTime(self, raw=False):
        if raw:
            return self.data['currently']['time']
        else:
            return time.ctime(self.data['currently']['time'])

    def getCurrentlySummary(self):
        return self.data['currently']['summary']

    def getCurrentlyIcon(self):
        return self.data['currently']['icon']

    def getCurrentlyNearestStormDistance(self):
        return self.data['currently']['nearestStormDistance']

    def getCurrentlyNearestStormBearing(self):
        try:
            return self.data['currently']['nearestStormBearing']
        except:
            return 0

    def getCurrentlyPrecipIntensity(self):
        return self.data['currently']['precipIntensity']

    def getCurrentlyPrecipIntensityError(self):
        return self.data['currently']['precipIntensityError']

    def getCurrentlyPrecipProbability(self):
        return self.data['currently']['precipProbability']

    def getCurrentlyPrecipType(self):
        return self.data['currently']['precipType']

    def getCurrentlyTemperature(self):
        return self.data['currently']['temperature']

    def getCurrentlyApparentTemperature(self):
        return self.data['currently']['apparentTemperature']

    def getCurrentlyDewPoint(self):
        return self.data['currently']['dewPoint']

    def getCurrentlyHumidity(self):
        return self.data['currently']['humidity']

    def getCurrentlyPressure(self):
        return self.data['currently']['pressure']

    def getCurrentlyWindSpeed(self):
        return self.data['currently']['windSpeed']

    def getCurrentlyWindGust(self):
        return self.data['currently']['windGust']

    def getCurrentlyWindBearing(self):
        return self.data['currently']['windBearing']

    def getCurrentlyCloudCover(self):
        return self.data['currently']['cloudCover']

    def getCurrentlyUVIndex(self):
        return self.data['currently']['uvIndex']

    def getCurrentlyVisibility(self):
        return self.data['currently']['visibility']

    def getCurrentlyOzone(self):
        return self.data['currently']['ozone']

    ''' Minutely data request '''
    def getMinutelySummary(self):
        return self.data['minutely']['summary']

    def getMinutelyIcon(self):
        return self.data['minutely']['icon']

    def getMinutelyDataCount(self):
        return len(self.data['minutely']['data'])

    def getMinutelyData(self, index=0):
        tm = time.ctime(self.data['minutely']['data'][index]['time'])
        precipIntensity = self.data['minutely']['data'][index]['precipIntensity']
##        precipIntensityError = self.data['minutely']['data'][index]['precipIntensityError']
        precipProbability = self.data['minutely']['data'][index]['precipProbability']
##        precipType = self.data['minutely']['data'][index]['precipType']
        return (tm, precipIntensity, precipProbability)

    ''' Hourly data request '''
    def getHourlySummary(self):
        return self.data['hourly']['summary']

    def getHourlyIcon(self):
        return self.data['hourly']['icon']

    def getHourlyDataCount(self):
        return len(self.data['hourly']['data'])

    def getHourlyData(self, index=0):
        tm = time.ctime(self.data['hourly']['data'][index]['time'])
        summary = self.data['hourly']['data'][index]['summary']
        icon = self.data['hourly']['data'][index]['icon']
        precipIntensity = self.data['hourly']['data'][index]['precipIntensity']
##        precipIntensityError = self.data['hourly']['data'][index]['precipIntensityError']
        precipProbability = self.data['hourly']['data'][index]['precipProbability']
##        precipType = self.data['hourly']['data'][index]['precipType']
        temperature = self.data['hourly']['data'][index]['temperature']
        apparentTemperature = self.data['hourly']['data'][index]['apparentTemperature']
        dewPoint = self.data['hourly']['data'][index]['dewPoint']
        humidity = self.data['hourly']['data'][index]['humidity']
        pressure = self.data['hourly']['data'][index]['pressure']
        windSpeed = self.data['hourly']['data'][index]['windSpeed']
        windGust = self.data['hourly']['data'][index]['windGust']
        windBearing = self.data['hourly']['data'][index]['windBearing']
        cloudCover = self.data['hourly']['data'][index]['cloudCover']
        uvIndex = self.data['hourly']['data'][index]['uvIndex']
        visibility = self.data['hourly']['data'][index]['visibility']
        ozone = self.data['hourly']['data'][index]['ozone']
        return (tm, summary, icon, precipIntensity, precipProbability,
                temperature, apparentTemperature, dewPoint, humidity, pressure,
                windSpeed, windGust, windBearing, cloudCover, uvIndex,
                visibility, ozone)

    ''' Daily data request '''
    def getDailySummary(self):
        return self.data['daily']['summary']

    def getDailyIcon(self):
        return self.data['daily']['icon']

    def getDailyDataCount(self):
        return len(self.data['daily']['data'])

    def getDailyData(self, index=0):
        tm = time.ctime(self.data['daily']['data'][index]['time'])
        summary = self.data['daily']['data'][index]['summary']
        icon = self.data['daily']['data'][index]['icon']
        sunriseTime = time.ctime(self.data['daily']['data'][index]['sunriseTime'])
        sunsetTime = time.ctime(self.data['daily']['data'][index]['sunsetTime'])
##        moonPhase = self.data['daily']['data'][index]['moonPhase']
        precipIntensity = self.data['daily']['data'][index]['precipIntensity']
        precipIntensityMax = self.data['daily']['data'][index]['precipIntensityMax']
        precipIntensityMaxTime = time.ctime(self.data['daily']['data'][index]['precipIntensityMaxTime'])
##        precipIntensityError = self.data['daily']['data'][index]['precipIntensityError']
        precipProbability = self.data['daily']['data'][index]['precipProbability']
##        precipType = self.data['daily']['data'][index]['precipType']
        temperatureHigh = self.data['daily']['data'][index]['temperatureHigh']
        temperatureHighTime = time.ctime(self.data['daily']['data'][index]['temperatureHighTime'])
        temperatureLow = self.data['daily']['data'][index]['temperatureLow']
        temperatureLowTime = time.ctime(self.data['daily']['data'][index]['temperatureLowTime'])
        apparentTemperatureHigh = self.data['daily']['data'][index]['apparentTemperatureHigh']
        apparentTemperatureHighTime = time.ctime(self.data['daily']['data'][index]['apparentTemperatureHighTime'])
        apparentTemperatureLow = self.data['daily']['data'][index]['apparentTemperatureLow']
        apparentTemperatureLowTime = time.ctime(self.data['daily']['data'][index]['apparentTemperatureLowTime'])
        dewPoint = self.data['daily']['data'][index]['dewPoint']
        humidity = self.data['daily']['data'][index]['humidity']
        pressure = self.data['daily']['data'][index]['pressure']
        windSpeed = self.data['daily']['data'][index]['windSpeed']
        windGust = self.data['daily']['data'][index]['windGust']
        windGustTime = time.ctime(self.data['daily']['data'][index]['windGustTime'])
        windBearing = self.data['daily']['data'][index]['windBearing']
        cloudCover = self.data['daily']['data'][index]['cloudCover']
        uvIndex = self.data['daily']['data'][index]['uvIndex']
        uvIndexTime = time.ctime(self.data['daily']['data'][index]['uvIndexTime'])
        visibility = self.data['daily']['data'][index]['visibility']
        ozone = self.data['daily']['data'][index]['ozone']
        temperatureMin = self.data['daily']['data'][index]['temperatureMin']
        temperatureMinTime = time.ctime(self.data['daily']['data'][index]['temperatureMinTime'])
        temperatureMax = self.data['daily']['data'][index]['temperatureMax']
        temperatureMaxTime = time.ctime(self.data['daily']['data'][index]['temperatureMaxTime'])
        apparentTemperatureMin = self.data['daily']['data'][index]['apparentTemperatureMin']
        apparentTemperatureMinTime = time.ctime(self.data['daily']['data'][index]['apparentTemperatureMinTime'])
        apparentTemperatureMax = self.data['daily']['data'][index]['apparentTemperatureMax']
        apparentTemperatureMaxTime = time.ctime(self.data['daily']['data'][index]['apparentTemperatureMaxTime'])
        return (tm, summary, icon, sunriseTime, sunsetTime, precipIntensity, precipIntensityMax,
                precipIntensityMaxTime, precipProbability, temperatureHigh, temperatureHighTime, 
                temperatureLow, temperatureLowTime, apparentTemperatureHigh, apparentTemperatureHighTime,
                apparentTemperatureLow, apparentTemperatureLowTime, dewPoint, humidity, pressure,
                windSpeed, windGust, windGustTime, windBearing, cloudCover, uvIndex, uvIndexTime,
                visibility, ozone, temperatureMin, temperatureMinTime, temperatureMax, temperatureMaxTime,
                apparentTemperatureMin, apparentTemperatureMinTime, apparentTemperatureMax, apparentTemperatureMaxTime)

    ''' Alerts '''
    def getAlertsCount(self):
        return len(self.data['alerts'])

    def getAlertsData(self, index=0):
        title = self.data['alerts'][index]['title']
        tm = time.ctime(self.data['alerts'][index]['time'])
        expires = time.ctime(self.data['alerts'][index]['expires'])
        description = self.data['alerts'][index]['description']
        uri = self.data['alerts'][index]['uri']
        return (title, tm, expires, description, uri)
    
    ''' Flags '''
    def getFlagsSources(self):
        return self.data['flags']['sources']

    def getFlagsNearestStation(self):
        return self.data['flags']['nearest-station']

    def getFlagsUnits(self):
        return self.data['flags']['units']

    ''' Print the results of each data collection '''
    def printCurrentlyWeatherData(self):
        time = self.getCurrentlyTime()
        summary = self.getCurrentlySummary()
        icon = self.getCurrentlyIcon()
##        nearestStormDistance = self.getCurrentlyNearestStormDistance()
##        nearestStormBearing = self.getCurrentlyNearestStormBearing()
        precipIntensity = self.getCurrentlyPrecipIntensity()
##        precipIntensityError = self.getCurrentlyPrecipIntensityError()
        precipProbability = self.getCurrentlyPrecipProbability()
##        precipType = self.getCurrentlyPrecipType()
        temperature = self.getCurrentlyTemperature()
        apparentTemperature = self.getCurrentlyApparentTemperature()
        dewPoint = self.getCurrentlyDewPoint()
        humidity = self.getCurrentlyHumidity()
        pressure = self.getCurrentlyPressure()
        windSpeed = self.getCurrentlyWindSpeed()
        windGust = self.getCurrentlyWindGust()
        windBearing = self.getCurrentlyWindBearing()
        cloudCover = self.getCurrentlyCloudCover()
        uvIndex = self.getCurrentlyUVIndex()
        visibility = self.getCurrentlyVisibility()
        ozone = self.getCurrentlyOzone()

        print('Time: {}\nSummary: {}\nIcon: {}\n' \
              # 'Nearest Storm Distance: {}\n' \
              # 'Nearest Storm Bearing: {}\n' \
              'Precipitation Intensity: {}\n' \
              'Precipitation Probability: {}\n' \
              'Temperature: {}\nApparent Temperature: {}\nDew Point: {}\n' \
              'Humidity: {}\nPressure: {}\nWind Speed: {}\nWind Gust: {}\n' \
              'Wind Bearing: {}\nCloud Cover: {}\nUV Index: {}\n' \
              'Visibility: {}\nOzone: {}'
              .format(time, summary, icon,
                      # nearestStormDistance,
                      # nearestStormBearing,
                      precipIntensity, precipProbability,
                      temperature, apparentTemperature, dewPoint, humidity,
                      pressure, windSpeed, windGust, windBearing, cloudCover,
                      uvIndex, visibility, ozone))

    def printMinutelyWeatherData(self):
        print('\nMinutely Weather Data...')
        print('Summary: {}, Icon: {}'.format(self.getMinutelySummary(),
                                             self.getMinutelyIcon()))
        for idx in range(0, self.getMinutelyDataCount()):
            print('Minutely[{}]: {}'.format(idx, self.getMinutelyData(index=idx)))

    def printHourlyWeatherData(self):
        print('\nHourly Weather Data...')
        print('Summary: {}, Icon: {}'.format(self.getHourlySummary(),
                                             self.getHourlyIcon()))
        for idx in range(0, self.getHourlyDataCount()):
            print('Hourly[{}]: {}'.format(idx, self.getHourlyData(index=idx)))

    def printDailyWeatherData(self):
        print('\nDaily Weather Data...')
        print('Summary: {}, Icon: {}'.format(self.getDailySummary(),
                                             self.getDailyIcon()))
        for idx in range(0, self.getDailyDataCount()):
            print('Daily[{}]: {}'.format(idx, self.getDailyData(index=idx)))

    def printAlerts(self):
        print('\nAlerts...')

        try:
            for idx in range(0, self.getAlertsCount()):
                print('Alert[{}]: {}'.format(idx, self.getAlertsData(index=idx)))
        except:
            print('Alert: None')

    def printFlags(self):
        print('\nSources: {}\nNearest Station: {}\nUnits: {}'.format(self.getFlagsSources(), self.getFlagsNearestStation(), self.getFlagsUnits()))
        
    def printForecastRequest(self):
        print('Current Weather Data = {}'.format(self.data))

    def saveForecastRequest(self):
        directory = 'data'
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        filename = 'forecast_request' + '-' + time.strftime("%Y%m%d") + '-' + time.strftime("%H%M%S") + '.json'
        with open(os.path.join(directory, filename), 'w') as write_data:
            write_data.write(str(self.data))

    def __str__(self):
        return 'Latitude: {}, Longitude: {}, Timezone: {}, Offset: {}'.format(self.getLatitude(), self.getLongitude(), self.getTimezone(), self.getOffset())


class TimeMachineRequest(ForecastRequest):

    def __init__(self, year='1970', month='01', date='01', hour='00', minute='00', second='00'):        
        ForecastRequest.__init__(self)
        self.year = year
        self.month = month
        self.date = date
        self.hour = hour
        self.minute = minute
        self.second = second

        self.data = self.getTimeMachineRequest()

    def getTimeMachineRequest(self):
        '''
        GET https://api.darksky.net/forecast/0123456789abcdef9876543210fedcba/42.3601,-71.0589,255657600?exclude=currently,flags
        
        Either be a UNIX time (that is, seconds since midnight GMT on 1 Jan 1970) or a string formatted as follows:
        [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS][timezone]. timezone should either be omitted (to refer to local time for
        the location being requested), Z (referring to GMT time), or +[HH][MM] or -[HH][MM] for an offset from
        GMT in hours and minutes. The timezone is only used for determining the time of the request; the response will
        always be relative to the local time zone.
        '''
        http_request = 'https://api.darksky.net/forecast/' + self.key + '/' + self.lat + ',' + self.lon + ',' + self.year + '-' + self.month + '-' + self.date + 'T' +  self.hour + ':' + self.minute + ':' + self.second
        # print('HTTP request: {}'.format(http_request))
        if self.proxies == None:
            res = requests.get(http_request)
        else:
            res = requests.get(http_request, proxies=self.proxies)
        return res.json()

    def printDailyWeatherData(self):        
        sunriseTime = time.ctime(self.data['daily']['data'][0]['sunriseTime'])
        sunsetTime = time.ctime(self.data['daily']['data'][0]['sunsetTime'])
        moonPhase = self.data['daily']['data'][0]['moonPhase']        
        print('Sunrise: {}\nSunset: {}\nMoon phase: {}'.format(sunriseTime, sunsetTime, moonPhase))
