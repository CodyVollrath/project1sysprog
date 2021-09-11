#!/usr/bin/env python3
"""
Validates the card value entered into it
"""

import re

__author__ = 'Cody Vollrath'
__version__ = 'Fall 2021'
__pylint__ = 'v1.8.3.'

def is_valid(sequence):
    """
    Validates Credit Cards
    Args: credit_card_number - the specified credit card number that is being checked
    Returns: a boolean indicating the validity of the credit card number
    """
    regex = r'^(\d{13,19})$|^(\d{4}-\d{4}-\d{4}-\d{4})$|^(\d{4} \d{4} \d{4} \d{4})$'
    credit_card_regex = re.compile(regex)
    if not credit_card_regex.match(sequence):
        return False
    return True


def determine_card_issuer(credit_card_number, data_map):
    """
    Determines the card issuer by cross referencing
    with the data map which contains the parsed csv data
    Args: credit_card_number & data_map
    - the credit card number and the parsed csv data respectfully
    Returns: the card issuer name if available, otherwise, None
    """
    card_issuer = None
    for key in data_map:
        data_detail = data_map[key]
        lengths = data_detail[0]
        prefixes = data_detail[1]
        if __is_length_of(credit_card_number, lengths)\
                and __prefix_matches(credit_card_number, prefixes):
            card_issuer = key
    return card_issuer

def luhn_verified(credit_card_number):
    """
    Performs Luhns Algorithim to determine if the card is an authentic card
    Args: credit_card_number - the credit card number
    Returns: true if authentic, false otherwise
    """
    last_digit = int(credit_card_number[-1])
    reverse_card = credit_card_number[-2::-1]
    processed_digits = []
    for i, digit in enumerate(reverse_card):
        if i % 2 == 0:
            double_digit = int(digit) * 2
            if double_digit > 9:
                double_digit = double_digit - 9
            processed_digits.append(double_digit)
        else:
            processed_digits.append(int(digit))

    total = last_digit + sum(processed_digits)
    return total % 10 == 0

def __is_length_of(credit_card_number, lengths):
    """
    Private helper to cross reference the list of
    potential lengths with the actual credit card number
    Returns: true if any length in the list matches, false otherwise
    """
    lengths = lengths.split(',')
    for length in lengths:
        if int(length) == len(credit_card_number):
            return True
    return False

def __prefix_matches(credit_card_number, prefixes):
    """
    Private helper to cross reference the list of potential
    prefixes with the starting numbers in the credit card number
    Returns: true if any prefix is at the start of the credit card number, false otherwise
    """
    prefixes = prefixes.split(',')
    for prefix in prefixes:
        if '-' in prefix:
            ranges = prefix.split('-')
            upper_range = int(ranges[1])
            lower_range = int(ranges[0])
            if int(credit_card_number[0:len(ranges[0])]) >= lower_range\
                    and int(credit_card_number[0:len(ranges[1])]) <= upper_range:
                        return True
        if credit_card_number.startswith(prefix):
            return True
    return False
