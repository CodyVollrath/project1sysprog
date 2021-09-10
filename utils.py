#!/usr/bin/env python3
"""
Validates the card value entered into it
"""

import re

__author__ = 'Cody Vollrath'
__version__ = 'Fall 2021'
__pylint__ = 'v1.8.3.'

def verify_credit_card(credit_card_number):
    """
    Validates Credit Cards
    Args: credit_card_number - the specified credit card number that is being checked
    Returns: a boolean indicating the validity of the credit card number
    """
    credit_card_regex = re.compile(r"""(\d{13,19})
           |(\d{4}-\d{4}-\d{4}-\d{4})
           |((\d{4} \d{4} \d{4} \d{4}))""", re.X)
    if not credit_card_regex.match(credit_card_number):
        return False
    return True

def get_file_data(filename):
    """
    Gets the file content from the file path that is passed into the function
    Returns: content of file if opened
    Raises: IOError if the file can not be opened and displays the error message
    """
    content = None
    try:
        with open(filename) as input_file:
            content = input_file.read()
        input_file.close()
        return content
    except IOError as error:
        print('Error:',  error)

def parse_csv(csv_str):
    """
    Takes the CSV data from the passed in string and converts it into a dict
    Args: csv_str - the csv string to be parsed
    returns the dict of the csv data
    """
    data_map = {}
    line_split_csv = csv_str.split('*')
    for element in line_split_csv:
        fields = element.split(';')
        data_map[fields[0]] = fields[1:]
    data_map.pop('')
    return data_map

def determine_card_issuer(credit_card_number, data_map):
    card_issuer = None
    for key in data_map:
        data_detail = data_map[key]
        lengths = data_detail[0]
        prefixes = data_detail[1]
        if __is_length_of(credit_card_number, lengths) and __prefix_matches(credit_card_number, prefixes):
            card_issuer = key
            return card_issuer
    return card_issuer

def __is_length_of(credit_card_number, lengths):
    lengths = lengths.split(',')
    for length in lengths:
        if int(length) == len(credit_card_number):
            return True
    return False
def __prefix_matches(credit_card_number, prefixes):
    prefixes = prefixes.split(',')
    for prefix in prefixes:
        if '-' in prefix:
            ranges = prefix.split('-')
            if int(credit_card_number[0:len(ranges[0]) + 1]) >= int(ranges[0]) and int(credit_card_number[0:len(ranges[1]) + 1]) <= int(ranges[1]):
                return True
        if credit_card_number.startswith(prefix):
            return True
    return False

