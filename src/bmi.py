#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""BMI class."""


class BMI:

    __weight = None
    __height = None
    __bmi = None
    __perfect_bmi = 21.75
    rate = 1

    def __init__(self, weight=None, height=None):
        """Init BMI class."""
        if weight is not None and isinstance(weight, (float, int)):
            self.__set_weight(weight)
        else:
            print('Wrong weight.')
        if height is not None and isinstance(height, float):
            self.__set_height(height)
        else:
            print('Wrong height.')

    def get_bmi(self):
        """Return BMI."""
        if self.__calculate() is True:
            return self.__bmi
        else:
            return False

    def norm(self):
        """Is BMI is in norm"""
        if self.__calculate() is True:
            if self.__bmi < (18.5 / self.rate):
                return -1
            elif self.__bmi >= (25 / self.rate):
                return 1
            else:
                return 0
        else:
            return False

    def get_correct_weight(self):
        """Get correct weight of body"""
        if self.__calculate() is True:
            if self.__bmi < (18.5 / self.rate):
                return (18.5 / self.rate) * (self.__height ** 2)
            elif self.__bmi >= (25 / self.rate):
                return (24.99 / self.rate) * (self.__height ** 2)
            else:
                return (self.__perfect_bmi / self.rate) * (self.__height ** 2)
        else:
            return False

    def __set_weight(self, person_weight):
        """Set width."""
        self.__weight = person_weight

    def __set_height(self, person_height):
        """Set height."""
        self.__height = person_height

    def __calculate(self):
        """Calculate BMI."""
        if self.__weight is not None and self.__height is not None:
            self.__bmi = (self.__weight / self.__height ** 2) / self.rate
            return True
        else:
            return False
