import json
import urllib.request 

map_city_to_coords = {
    'Abuja': 'lat=9.0764785&lon=7.398574',
    'Nairobi': 'lat=-1.2920659&lon=36.8219462',
    'Accra': "lat=5.6037168&lon=-0.1869644",
    'Rabat': 'lat=34.020882&lon=-6.84165'
}
        
def show_weather_to_user(weather_data_list):
    for weather_data in weather_data_list:
        hour_number = weather_data['timepoint']
        temperature = weather_data['temp2m']
        wind_direction = weather_data['wind10m']['direction']
        print(f'On hour {hour_number},')
        if hour_number == 24:
            print('(in one day)')
        elif hour_number == 48:
            print('(in two days)')
        elif hour_number == 72:
            print('(in three days)')
        
        if wind_direction == 'E':
            wind_direction = 'East'
        elif wind_direction == 'S':
            wind_direction = 'South'
        elif wind_direction == 'N':
            wind_direction = 'North'
        elif wind_direction == 'W':
            wind_direction = 'West'
        elif wind_direction == 'NW':
            wind_direction = 'NorthWest'
        elif wind_direction == 'SW':
            wind_direction = 'SouthWest'
        elif wind_direction == 'SE':
            wind_direction = 'SouthEast'
        elif wind_direction == 'NE':
            wind_direction = 'NorthEast'
        print(f'The windirection is from the {wind_direction}')
        print(f'The temperature is {temperature}')

def show_weather():
    city_name = input('Please type a city: ')
    if city_name not in map_city_to_coords:
        print('We do not have coordinates for that city.')
    else:
        get_api_results(city_name)
        with open('api_output.json', 'r') as f:
            all_data = json.load(f)
            weather_data_list = all_data['dataseries']
        
        
        show_weather_to_user(weather_data_list)



def get_api_results(city):
    coords = map_city_to_coords[city]
    url = ('https://www.7timer.info/bin/astro.php?' + 
        f'{coords}&ac=0&unit=metric&output=json')
    results = urllib.request.urlopen(url)
    json_content = results.read().decode('utf-8')
    with open('api_output.json', 'w') as f:
        f.write(json_content)

show_weather()
