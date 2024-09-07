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


def main():

    filename = "SQLite.db"

    if not databaseExist(filename):
        createDatabase(filename)

    w_data = OpenWeatherMap.CurrentWeatherData()
    w_data.printCurrentWeatherData()
    w_data.saveCurrentWeatherData()
    add(filename, w_data)

if __name__ == '__main__':
    main()
