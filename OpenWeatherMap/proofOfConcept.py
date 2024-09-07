#!/usr/bin/env python3
import os
import sqlite3
import time
import datetime
import requests
import OpenWeatherMap


def databaseExist(filename):
    return os.path.exists(filename)


def createDatabase(filename):

    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE weather (
            [coord.lon]           REAL,
            [coord.lat]           REAL,
            [weather.id]          INTEGER,
            [weather.main]        TEXT,
            [weather.description] TEXT,
            [weather.icon]        TEXT,
            base                  TEXT,
            [main.temp]           REAL,
            [main.pressure]       REAL,
            [main.humidity]       REAL,
            [main.temp_min]       REAL,
            [main.temp_max]       REAL,
            [main.sea_level]      REAL,
            [main.grnd_level]     REAL,
            visibility            REAL,
            [wind.speed]          REAL,
            [wind.gust]           REAL,
            [wind.deg]            REAL,
            [clouds.all]          REAL,
            [rain.1h]             REAL,
            [rain.3h]             REAL,
            [snow.1h]             REAL,
            [snow.3h]             REAL,
            dt                    NUMERIC,
            [sys.type]            INTEGER,
            [sys.id]              INTEGER,
            [sys.message]         REAL,
            [sys.country]         TEXT,
            [sys.sunrise]         NUMERIC,
            [sys.sunset]          NUMERIC,
            timezone              INTEGER,
            id                    INTEGER,
            name                  TEXT,
            cod                   INTEGER
        );
    """)
    conn.commit()
    cur.close()


def add(dbname, result):
    print(result)
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("INSERT INTO weather (\
                [coord.lon], \
                [coord.lat], \
                [weather.id], \
                [weather.main], \
                [weather.description], \
                [weather.icon], \
                base, \
                [main.temp], \
                [main.pressure], \
                [main.humidity], \
                [main.temp_min], \
                [main.temp_max], \
                visibility, \
                [wind.speed], \
                [wind.gust], \
                [wind.deg], \
                [clouds.all], \
                [rain.1h], \
                dt, \
                [sys.type], \
                [sys.id], \
                [sys.country], \
                [sys.sunrise], \
                [sys.sunset], \
                timezone, \
                id, \
                name, \
                cod ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                result['coord']['lon'],
                result['coord']['lat'],
                result['weather'][0]['id'],
                result['weather'][0]['main'],
                result['weather'][0]['description'],
                result['weather'][0]['icon'],
                result['base'],
                result['main']['temp'],
                result['main']['pressure'],
                result['main']['humidity'],
                result['main']['temp_min'],
                result['main']['temp_max'],
                result['visibility'],
                result['wind']['speed'],
                # result['wind']['gust'],
                0,
                result['wind']['deg'],
                result['clouds']['all'],
                # result['rain']['1h'],
                0,
                result['dt'],
                result['sys']['type'],
                result['sys']['id'],
                result['sys']['country'],
                result['sys']['sunrise'],
                result['sys']['sunset'],
                result['timezone'],
                result['id'],
                result['name'],
                result['cod']
        )
    )
    conn.commit()
    cur.close()

def add_v2(dbname, result):
    print(result)
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("INSERT INTO weather (\
                [coord.lon], \
                [coord.lat], \
                [weather.id], \
                [weather.main], \
                [weather.description], \
                [weather.icon], \
                base, \
                [main.temp], \
                [main.pressure], \
                [main.humidity], \
                [main.temp_min], \
                [main.temp_max], \
                visibility, \
                [wind.speed], \
                [wind.gust], \
                [wind.deg], \
                [clouds.all], \
                [rain.1h], \
                [rain.3h], \
                [snow.1h], \
                [snow.3h], \
                dt, \
                [sys.type], \
                [sys.id], \
                [sys.country], \
                [sys.sunrise], \
                [sys.sunset], \
                timezone, \
                id, \
                name, \
                cod ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, \
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?)", (
                result.getLongitude(),
                result.getLatitude(),
                result.getWeatherId(),
                result.getWeatherMain(),
                result.getWeatherDescription(),
                result.getWeatherIcon(),
                result.getBase(),
                result.getMainTemperature(),
                result.getMainPressure(),
                result.getMainHumidity(),
                result.getMainTemperatureMinimal(),
                result.getMainTemperatureMaximal(),
                result.getVisibility(),
                result.getWindSpeed(),
                result.getWindGust(),
                result.getWindBearing(),
                result.getCloudsAll(),
                result.getRain1H(),
                result.getRain3H(),
                result.getSnow1H(),
                result.getSnow3H(),
                result.getDate(),
                result.getSystemType(),
                result.getSystemId(),
                result.getSystemCountry(),
                result.getSystemSunrise(),
                result.getSystemSunset(),
                result.getTimezone(),
                result.getId(),
                result.getName(),
                result.getCod()
        )
    )
    conn.commit()
    cur.close()

def view(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    for row in cur.execute("select * from weather"):
        print(row)
    conn.commit()
    cur.close()


def weather_data(query):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=1234567890abcdef1234567890abcdef&units=metric')
    return res.json()


def print_weather(result, city):
    directory = 'data'
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = city + "-" + time.strftime("%Y%m%d") + "-" + time.strftime("%H%M%S") + ".json"
    with open(os.path.join(directory, filename), 'w') as write_weather:
        write_weather.write(str(result))

    weather = result['weather'][0]['main']

    print("{}'s current weather report...".format(city))
    print("Current temperature: {}°C ".format(result['main']['temp']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Pressure: {} hPa".format(result['main']['pressure']))
    print("Humidity: {}% ".format(result['main']['humidity']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    try:
        print("Wind gust: {} m/s".format(result['wind']['gust']))
    except:
        True  # do nothing
    try:
        print("Wind direction: {}°".format(result['wind']['deg']))
    except:
        True  # do nothing
    print("Clouds: {}%".format(result['clouds']['all']))
    print("Visibility: {:.2f} m".format(result['visibility']))
    print("Weather: {}".format(result['weather'][0]['main']))
    if weather in ['Drizzle', 'Rain', 'Thunderstorm']:
        try:
            print("Rain 1H, mm: {}".format(result['rain']['1h']))
        except:
            print("Rain 1H, mm: Not available")
        try:
            print("Rain 3H, mm: {}".format(result['rain']['3h']))
        except:
            print("Rain 3H, mm: Not available")
    if weather in ['Snow']:
        try:
            print("Snow 1H, mm: {}".format(result['snow']['1h']))
        except:
            print("Snow 1H, mm: Not available")
        try:
            print("Snow 3H, mm: {}".format(result['snow']['3h']))
        except:
            print("Snow 3H, mm: Not available")
    print("Sunrise: {}".format(time.ctime(result['sys']['sunrise'])))
    print("Sunset: {}".format(time.ctime(result['sys']['sunset'])))
    print("last updated: {}".format(datetime.datetime.fromtimestamp(result['dt'])))


def uvi_data(lat, lon):
    res = requests.get('http://api.openweathermap.org/data/2.5/uvi?&APPID=fa1c34476c3c0d5342b728022056eb74&lat=' + lat + '&lon=' + lon)
    return res.json()


def print_uvi(result, city):

    directory = 'uvi_data'
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = city + "-" + time.strftime("%Y%m%d") + "-" + time.strftime("%H%M%S") + ".json"
    with open(os.path.join(directory, filename), 'w') as write_weather:
        write_weather.write(str(result))

    print("{}'s uvi report...".format(city))
    print("Current value: {} ".format(result['value']))
    print("Latitude: {} ".format(result['lat']))
    print("Longitude: {} ".format(result['lon']))
    print("Date ISO: {} ".format(result['date_iso']))
    print("Date: {} ".format(datetime.datetime.fromtimestamp(result['date'])))

def main():

    filename = "SQLite.db"

    if not databaseExist(filename):
        createDatabase(filename)

    city = input('Enter the city: ')
    print()
    try:
        query = 'q=' + city
        w_data = weather_data(query)
        print_weather(w_data, city)
        print()
##        u_data = uvi_data(lat='34.073662', lon='-84.677101')
##        print_uvi(u_data, city)
        add(filename, w_data)
    except Exception as e:
        print('City name not found...')
        print(e)

def main_v2():

    filename = "SQLite.db"

    if not databaseExist(filename):
        createDatabase(filename)

    w_data = OpenWeatherMap.CurrentWeatherData()
    w_data.printCurrentWeatherData()
    w_data.saveCurrentWeatherData()
    add_v2(filename, w_data)

if __name__ == '__main__':
    main_v2()
