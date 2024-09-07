from DarkSky import TimeMachineRequest
import argparse

def main():

    cmd_parser = argparse.ArgumentParser(description='Get the time machine request')
    cmd_parser.add_argument('-p', action='store_true', help='print the forecast request')
    cmd_parser.add_argument('-s', action='store_true', help='save the forecast request to a json file')
    cmd_parser.add_argument('-H', action='store_true', help='print the hourly forecast request')
    cmd_parser.add_argument('-D', action='store_true', help='print the daily forecast request')
    cmd_parser.add_argument('-F', action='store_true', help='print the flags ')

    args = cmd_parser.parse_args()

    year = input('Year [YYYY]: ')
    month = input('Month [MM]: ')
    date = input('Date [DD]: ')
    hour = input('Hour [HH]: ')
    minute = input('Minute [MM]: ')
    second = input('Second [SS]: ')

    tm = TimeMachineRequest(year, month, date, hour, minute, second)
    print(tm)
    tm.printCurrentlyWeatherData()

    if args.p:        
        tm.printForecastRequest()
        print()

    if args.s:
        tm.saveForecastRequest()
        print()

    if args.H:        
        tm.printHourlyWeatherData()
        print()

    if args.D:
        tm.printDailyWeatherData()
        print()

    if args.F:
        tm.printFlags()
        print()
        
    print('Powered by Dark Sky: https://darksky.net/poweredby/')


if __name__ == '__main__':
    main()
