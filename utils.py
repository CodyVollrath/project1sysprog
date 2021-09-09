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
