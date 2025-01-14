"""
******************************
CS 1026 - Assignment 4 – Air Travel
Code by: Yiwei Dong
Student ID: ydong445
File created: December 4, 2024
******************************
This file defines the Airport class used to represent an airport with a code, city, and country.
"""

class Airport:

    def __init__(self, code, city, country): #set code, city, country init
        self._code = code
        self._city = city
        self._country = country

    def __str__(self): #set str return as code (city, country)
        return f"{self._code} ({self._city}, {self._country})"

    def __eq__(self, other): #set equal
        if isinstance(other, Airport):
            return self._code == other._code
        return False

    def get_code(self):
        return self._code

    def get_city(self):
        return self._city

    def get_country(self):
        return self._country

    def set_city(self, city):
        self._city = city

    def set_country(self, country):
        self._country = country
