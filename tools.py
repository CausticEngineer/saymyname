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
    # return dict of possible variants, example {'H': 4, 'Ti': 0}
    pass


def choose_best(vars_dict):
    # choosing the best looking element and it`s position
    # return a tuple, example ('Ti', 0)
    pass
