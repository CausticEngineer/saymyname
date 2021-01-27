import json
import cv2
#import numpy as np


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
        output = []
        pass
    else:
        if vars_list[0][0] == vars_list[1][0]:
            output = vars_list[1]
        else:
            output = vars_list[0]
    return output


def say_my_name(full_name):
    # breakingbadify a given name
    output = []
    names = full_name.split()
    for name in names:        
        finded_elements = find_bb_in_name(name)
        best_element = choose_best(finded_elements)
        output.append((best_element))
        print(' '.join([name[:best_element[0]], best_element[1], name[best_element[0]+len(best_element[1]):]]))
        print(best_element)
    return output


def make_picture(background, full_name):
    elements_with_position = say_my_name(full_name)
    img = cv2.imread(background)
    size = img.shape/10
    draw_chemical_element(img, elements_with_position[0][1], size)
    draw_chemical_element(img, elements_with_position[1][1], size)
    cv2.imwrite(f'{full_name}_{background}.jpg', img)

def draw_chemical_element(img, element, size):
    pass