#!/usr/bin/env python3

"""
Entry point for the project 1 assignment
"""
import sys
import utils
import csv_parser as parser

__author__ = 'Cody Vollrath'
__version__ = 'Fall 2021'
__pylint__ = '1.8.3.'

def format_output(credit_card_number, credit_card_issuer, luhn_verification):
    """
    Displays the final output of the program
    Args: credit_card_number
    & credit_card_issuer
    & luhn_verification the data fields to display to the user
    """
    print(f'Credit card number: \t{credit_card_number}')
    print(f'Credit card type: \t{credit_card_issuer}')
    print(f'Luhn verification: \t{luhn_verification}.')


def main():
    """
    Run function for the project 1 assignment
    Args: - credit_card_number the credit card number entered by the user
    """
    content = parser.get_file_data(sys.argv[1]).replace('\n', '*')
    credit_card_number = input('Please enter a credit card number:\n ')\
            .replace(' ', '').replace('-', '').strip()
    credit_card_type = 'Invalid'
    luhn_verification = 'N/A'
    if utils.is_valid(credit_card_number):
        data_map = parser.parse_csv(content)
        credit_card_type = utils.determine_card_issuer(credit_card_number, data_map)
        is_authentic = utils.luhn_verified(credit_card_number)
        luhn_verification = 'Authentic' if is_authentic else 'Fake'
    else:
        credit_card_number = 'Invalid'
    format_output(credit_card_number, credit_card_type, luhn_verification)

if __name__ == '__main__':
    main()
