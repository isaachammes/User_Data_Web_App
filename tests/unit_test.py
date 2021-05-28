import pytest
import json
from helpers import *

test_data_count = {
        'total_users': 5, \
        'count_female': 4, \
        'count_by_state': {'Extremadura': 1, 'Kansas': 1, 'Minas Gerais': 1, 'Nord-TrÃ¸ndelag': 1, 'Victoria': 1}, \
        'count_female_by_state': {'Extremadura': 0, 'Kansas': 1, 'Minas Gerais': 1, 'Nord-TrÃ¸ndelag': 1, 'Victoria': 1}, \
        'count_male_by_state': {'Extremadura': 1, 'Kansas': 0, 'Minas Gerais': 0, 'Nord-TrÃ¸ndelag': 0, 'Victoria': 0}, \
        'count_by_first_name_start_letter': {'A-M': 4, 'N-Z': 1}, \
        'count_by_last_name_start_letter': {'A-M': 3, 'N-Z': 2}, \
        'count_by_age': {'0-20': 0, '21-40': 3, '41-60': 1, '61-80': 1, '81-100': 0, '>100': 0},
    }

test_population_percentage_by_state = {'Extremadura': 20.0, 'Kansas': 20.0, 'Minas Gerais': 20.0, 'Nord-TrÃ¸ndelag': 20.0, 'Victoria': 20.0}
test_sex_percentage_by_state  = {'Extremadura': 100.0, 'Kansas': 0.0, 'Minas Gerais': 0.0, 'Nord-TrÃ¸ndelag': 0.0, 'Victoria': 0.0}
test_age_percentage = {'0-20': 0.0, '21-40': 60.0, '41-60': 20.0, '61-80': 20.0, '81-100': 0.0, '>100': 0.0}
test_total_users = test_data_count['total_users']

def test_process_users():
    f = open('test.json')
    test_data = json.load(f)['results']
    f.close()
    assert process_users(test_data) == test_data_count

def test_get_population_percentage_by_state():
    assert get_population_percentage_by_state(test_data_count['count_by_state'], test_total_users) == test_population_percentage_by_state

def test_get_sex_percentage_by_state():
    assert get_sex_percentage_by_state(test_data_count['count_male_by_state'], test_data_count['count_by_state']) == test_sex_percentage_by_state

def test_get_percentage_by_age():
    assert get_percentage_by_age(test_data_count['count_by_age'], test_total_users) == test_age_percentage

def test_get_percent():
    part = 3
    whole = 9
    assert get_percent(part, whole) == 33.3

def test_dictionary_sort_by_value():
    unsorted_dict = {"A":0, "B":4, "C":3}
    assert dictionary_sort_by_value(unsorted_dict) == {"B":4, "C":3, "A":0}