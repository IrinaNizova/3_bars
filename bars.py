import json
import math
import argparse


def load_data(filepath):
    with open(filepath) as bars_info:
        return json.loads(bars_info.read())

def get_biggest_bar(bars_list):
    return max(bars_list, key=lambda p: p["properties"]["Attributes"]["SeatsCount"])


def get_smallest_bar(bars_list):
    return min(bars_list, key=lambda p: p["properties"]["Attributes"]["SeatsCount"])


def get_closest_bar(bars_list, longitude, latitude):
    coords = [(bar["geometry"]["coordinates"],
               bar["properties"]["Attributes"]["Name"])
              for bar in bars_list]
    distances = []
    for coord in coords:
        distance = math.sqrt((float(coord[0][0]) - longitude) ** 2
                             + (float(coord[0][1]) - latitude) ** 2)
        distances.append((distance, coord[1]))
    return min(distances)[1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="write name of json file")
    bars_list = load_data(parser.parse_args().file_name)["features"]
    biggest_bar_info = get_biggest_bar(bars_list)
    print('Самый большой бар {} включает {} посадочных мест'
          .format(biggest_bar_info["properties"]["Attributes"]["Name"], 
                  biggest_bar_info["properties"]["Attributes"]["SeatsCount"]))
    smallest_bar_info = get_smallest_bar(bars_list)
    print('Самый маленький бар {} включает {} посадочных мест'
          .format(smallest_bar_info["properties"]["Attributes"]["Name"], 
                  smallest_bar_info["properties"]["Attributes"]["SeatsCount"]))
    print('Вы можете ввести свои координаты чтобы найти ближайший бар')
    longitude = float(input('Введине долготу: '))
    latitude = float(input('Введите широту: '))
    print('Ближайший бар это {}'.format(get_closest_bar(bars_list, longitude, latitude)))
