#!/usr/bin/env python3

"""
Entry point for the project 1 assignment
"""
import sys
import utils

__author__ = 'Cody Vollrath'
__version__ = 'Fall 2021'
__pylint__ = '1.8.3.'
 
def main():
    """
    Run function for the project 1 assignment
    Args: - credit_card_number the credit card number entered by the user
    """
    content = utils.get_file_data(sys.argv[1]).replace('\n','*')
    credit_card_number = input("Please enter a credit card number: ")
    if utils.verify_credit_card(credit_card_number):
        data_map = utils.parse_csv(content)
        credit_card_type = utils.determine_card_issuer(credit_card_number, data_map)
        print(credit_card_type)

if __name__ == '__main__':
    main()
