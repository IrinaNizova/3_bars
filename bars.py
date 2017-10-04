import json
import math


def load_data(filepath):
    with open(filepath) as bars_info:
        return json.loads(bars_info.read())


def get_biggest_bar(data):
    return max([(d["properties"]["Attributes"]["SeatsCount"], d["properties"]["Attributes"]["Name"]) for d in data],
               key=lambda p: p[0])


def get_smallest_bar(data):
    return min([(d["properties"]["Attributes"]["SeatsCount"], d["properties"]["Attributes"]["Name"]) for d in data],
               key=lambda p: p[0])


def get_closest_bar(data, longitude, latitude):
    coords = [(d["geometry"]["coordinates"], d["properties"]["Attributes"]["Name"]) for d in data]
    distances = []
    for coord in coords:
        distance = math.sqrt((float(coord[0][0]) - longitude) ** 2 + (float(coord[0][1]) - latitude) ** 2)
        distances.append((distance, coord[1]))
    return min(distances)[1]


if __name__ == '__main__':
    bars_list = load_data('bars.json')["features"]
    biggest_bar_info = get_biggest_bar(bars_list)
    print('Biggest bar is {} which has {} seats'.format(biggest_bar_info[1], biggest_bar_info[0]))
    smallest_bar_info = get_smallest_bar(bars_list)
    print('Smallest bar is {} which has {} seats'.format(smallest_bar_info[1], smallest_bar_info[0]))
    print('If you want to find closest bar, input your coordinates')
    longitude = float(input('input longitude: '))
    latitude = float(input('input latitude: '))
    print('Closest bar is {}'.format(get_closest_bar(bars_list, longitude, latitude)))
