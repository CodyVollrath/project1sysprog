#!/usr/bin/env python3

"""
Entry point for the project 1 assignment
"""
import sys
import utils

__author__ = 'Cody Vollrath'
__version__ = 'Fall 2021'
__pylint__ = '1.8.3.'


def get_resource():
    """
    Reads from the path to file as input from the command line args
    Returns: content of the file
    """
    content = None
    try:
        with open(sys.argv[1]) as input_file:
            content = input_file.read()
        input_file.close()
        return content
    except IOError as error:
        print('Error:',  error)

def main():
    """
    Run function for the project 1 assignment
    Args: - credit_card_number the credit card number entered by the user
    """
    content = get_resource();
    credit_card_number = input("Please enter a credit card number: ")
    if utils.verify_credit_card(credit_card_number):
        print("Valid Credit Card!")
    else:
        print("Invalid Credit Card!")


if __name__ == '__main__':
    main()
