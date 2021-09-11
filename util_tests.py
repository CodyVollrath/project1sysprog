#!/usr/bin/env python3
"""
Ensure correct functionality of module Utils
"""
import unittest
import utils
import csv_parser as parser

__author__ = 'Cody Vollrath'
__version__ = 'Fall 2021'
__pylint__ = '1.8.3'

class TestIsValidCreditCard(unittest.TestCase):
    """
    Tests public method is_valid for utils.py
    """
    def test_invalid_card_short(self):
        """
        Test invalid card number as too short
        """
        card_number = '1234'
        self.assertFalse(utils.is_valid(card_number))

    def test_invalid_card_long(self):
        card_number = '41021234123412341123111'
        self.assertFalse(utils.is_valid(card_number))

    def test_valid_card_no_spaces(self):
        card_number = '4102123412341234'
        self.assertTrue(utils.is_valid(card_number))

    def test_valid_card_spaces(self):
        card_number = '4102 1234 1234 1234'
        self.assertTrue(utils.is_valid(card_number))

    def test_valid_card_hyphens(self):
        card_number = '4102-1234-1234-1234'
        self.assertTrue(utils.is_valid(card_number))

class TestGetCardIssuer(unittest.TestCase):
    """
    Tests public method determine_card_issuer for utils.py
    """
    def test_no_card_issuer(self):
        card_number = '1234123412341234'
        file_data = parser.get_file_data('credit_card_types.ssv').replace('\n','*')
        parsed_csv = parser.parse_csv(file_data)
        self.assertTrue(utils.determine_card_issuer(card_number, parsed_csv) == None)

    def test_amex(self):
        card_number = '378282246310005'
        file_data = parser.get_file_data('credit_card_types.ssv').replace('\n','*')
        parsed_csv = parser.parse_csv(file_data)
        self.assertTrue(utils.determine_card_issuer(card_number, parsed_csv) == 'AmericanExpress')

    def test_verve_lowerrange(self):
        card_number = '5060991234561234'
        file_data = parser.get_file_data('credit_card_types.ssv').replace('\n','*')
        parsed_csv = parser.parse_csv(file_data)
        self.assertTrue(utils.determine_card_issuer(card_number, parsed_csv) == 'Verve')
    
    def test_verve_midrange(self):
        card_number = '5061001234561230'
        file_data = parser.get_file_data('credit_card_types.ssv').replace('\n','*')
        parsed_csv = parser.parse_csv(file_data)
        self.assertTrue(utils.determine_card_issuer(card_number, parsed_csv) == 'Verve')
        
    def test_verve_upperrange(self):
        card_number = '5061981234561230'
        file_data = parser.get_file_data('credit_card_types.ssv').replace('\n','*')
        parsed_csv = parser.parse_csv(file_data)
        self.assertTrue(utils.determine_card_issuer(card_number, parsed_csv) == 'Verve')

    def test_visa(self):
        card_number = '4012123412341234'
        file_data = parser.get_file_data('credit_card_types.ssv').replace('\n','*')
        parsed_csv = parser.parse_csv(file_data)
        self.assertTrue(utils.determine_card_issuer(card_number, parsed_csv) == 'Visa')

    def test_visa_electron(self):
        card_number = '4026123412341234'
        file_data = parser.get_file_data('credit_card_types.ssv').replace('\n','*')
        parsed_csv = parser.parse_csv(file_data)
        self.assertTrue(utils.determine_card_issuer(card_number, parsed_csv) == 'VisaElectron')

class TestLuhnAlgorithim(unittest.TestCase):
    """
    Tests the public method luhn_verified for utils.py
    """
    def test_fake(self):
        """
        Test fake card
        """
        card_number = '4026123412341235'
        self.assertFalse(utils.luhn_verified(card_number))
    
    def test_valid(self):
        """
        Test authentic card
        """
        card_number = '6703444444444449'
        self.assertTrue(utils.luhn_verified(card_number))
 
if __name__ == '__main__':
    unittest.main()
