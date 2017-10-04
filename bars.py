import json
import math


def load_data(filepath):
    with open(filepath) as bars_info:
        return json.loads(bars_info.read())


def get_biggest_bar(bars_data):
    return max([(bar_data["properties"]["Attributes"]["SeatsCount"], bar_data["properties"]["Attributes"]["Name"])
                for bar_data in bars_data], key=lambda p: p[0])


def get_smallest_bar(bars_data):
    return min([(bar_data["properties"]["Attributes"]["SeatsCount"], bar_data["properties"]["Attributes"]["Name"])
                for bar_data in bars_data], key=lambda p: p[0])


def get_closest_bar(bars_data, longitude, latitude):
    coords = [(bar_data["geometry"]["coordinates"], bar_data["properties"]["Attributes"]["Name"])
              for bar_data in bars_data]
    distances = []
    for coord in coords:
        distance = math.sqrt((float(coord[0][0]) - longitude) ** 2 + (float(coord[0][1]) - latitude) ** 2)
        distances.append((distance, coord[1]))
    return min(distances)[1]


if __name__ == '__main__':
    bars_list = load_data('bars.json')["features"]
    biggest_bar_info = get_biggest_bar(bars_list)
    print('Самый большой бар {} включает {} посадочных мест'.format(biggest_bar_info[1], biggest_bar_info[0]))
    smallest_bar_info = get_smallest_bar(bars_list)
    print('Самый маленький бар {} включает {} посадочных мест'.format(smallest_bar_info[1], smallest_bar_info[0]))
    print('Вы можете ввести свои координаты чтобы найти ближайший бар')
    longitude = float(input('Введине долготу: '))
    latitude = float(input('Введите широту: '))
    print('Ближайший бар это {}'.format(get_closest_bar(bars_list, longitude, latitude)))
