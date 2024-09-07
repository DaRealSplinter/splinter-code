#!/usr/bin/env python3
import DarkSky
import argparse

def main():

    cmd_parser = argparse.ArgumentParser(description='Get the weather forecast')
    cmd_parser.add_argument('-p', action='store_true', help='print the forecast request')
    cmd_parser.add_argument('-s', action='store_true', help='save the forecast request to a json file')
    cmd_parser.add_argument('-M', action='store_true', help='print the minutely forecast request')
    cmd_parser.add_argument('-H', action='store_true', help='print the hourly forecast request')
    cmd_parser.add_argument('-D', action='store_true', help='print the daily forecast request')
    cmd_parser.add_argument('-F', action='store_true', help='print the flags ')

    args = cmd_parser.parse_args()

    # always print (lat, lon), timezone, offset; currently data; weather alerts
    acworth = DarkSky.ForecastRequest()
    print(acworth)  # prints (lat, lon), timezone, offset
    acworth.printCurrentlyWeatherData()  # print the currently forecast
    acworth.printAlerts()  # print any forecast weather alerts

    if args.p:
        acworth.printForecastRequest()  # prints requested JSON file
        print()
    
    if args.s:
        acworth.saveForecastRequest()  # saves requested JSON file to folder
        print()

    if args.M:
        acworth.printMinutelyWeatherData()
        print()

    if args.H:
        acworth.printHourlyWeatherData()
        print()

    if args.D:
        acworth.printDailyWeatherData()
        print()

    if args.F:
        acworth.printFlags()
        print()

    print('Powered by Dark Sky: https://darksky.net/poweredby/')
    
    
if __name__ == '__main__':
    main()
