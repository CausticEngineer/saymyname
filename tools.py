import json
import cv2
import numpy as np


def load_elements(json_file):
    # load file and extract massive of elements with its features
    # example [['H', 'Hydrogen', 1, 1],['He', 'Helium', 2, 4]]
    pass


def find_bb_in_name(name):
    # finding chemical elements in a given single word
    # return dict of possible variants, example {'H': 4, 'Ti': 0}
    pass


def choose_best(vars_dict):
    # choosing the best looking element and it`s position
    # return a tuple, example ('Ti', 0)
    pass
