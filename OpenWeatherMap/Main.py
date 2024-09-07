#!/usr/bin/env python3
import OpenWeatherMap
import argparse

def main():

    cmd_parser = argparse.ArgumentParser(description='Get the weather forecast')
    cmd_parser.add_argument('-p', action='store_true', help='print the forecast request')
    cmd_parser.add_argument('-s', action='store_true', help='save the forecast request to a json file')
    cmd_parser.add_argument('-v', action='store_true', help='view the forecast request')

    args = cmd_parser.parse_args()

    # always print the current weather report
    acworth = OpenWeatherMap.CurrentWeatherData()
    acworth.printCurrentWeatherReport()

    if args.p:
        acworth.printCurrentWeatherData()
        print()

    if args.s:
        acworth.saveCurrentWeatherData()
        print()

    if args.v:
        print(acworth)
        print()
    
    print('Powered by Open Weather Map: https://openweathermap.org/')
    
    
if __name__ == '__main__':
    main()
