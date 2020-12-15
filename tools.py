import json
import cv2
import numpy as np


def load_elements(json_file):
    # load file and extract massive of elements with its features
    # example { "H": { "name": "Hydrogen", "number": 1, "atomic_mass": 1}, ...}
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data


def find_bb_in_name(name):
    # finding chemical elements in a given single word
    # return dict of possible variants
    # example [[0, 'Ti'], [1, 'I'], [2, 'K'], [3, 'H'], [3, 'Ho'], [4, 'O'], [5, 'N'], [5, 'No'], [7, 'V']]
    elements = list(load_elements('PeriodicTableJSON_lite.json').keys())
    element_entries = []
    for element in elements:
        position = name.lower().find(element.lower())
        if position != -1:
            element_entries.append([position, element])
    return sorted(element_entries)


def choose_best(vars_list):
    # choosing the best looking element and its position
    # return a list, example [0, 'Ti']
    if len(vars_list) == 0:
        print('Empty_list')
        break
    else:
        if vars_list[0][0] == vars_list[1][0]:
            output = vars_list[1]
        else:
            output = vars_list[0]
    return output
