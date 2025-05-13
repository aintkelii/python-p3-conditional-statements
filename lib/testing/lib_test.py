#!/usr/bin/env python3

from control_flow import admin_login, hows_the_weather, fizzbuzz, calculator

import io
import sys

class TestAdminLogin:
    '''admin_login() in control_flow.py'''

    def test_returns_access_granted_admin12345(self):
        '''returns "Access granted" for username=admin and password=12345'''
       
    def test_returns_access_granted_ADMIN12345(self):
        '''returns "Access granted" for username=ADMIN and password=12345'''
    

    def test_returns_access_denied_not_admin12345(self):
        '''returns "Access denied" for username!=admin or password!=12345'''
   
class TestHowsTheWeather:
    '''hows_the_weather() in control_flow.py'''

    def test_under_40_brisk(self):
        '''returns "It's brisk out there" for temperature=33'''
        
    def test_under_65_chilly(self):
        '''returns "It's a little chilly out there!" for temperature=55'''
       
    def test_above_85_too_dang_hot(self):
        '''returns "It's too dang hot out there!" for temperature=99'''
        
    def test_65_to_85_perfect(self):
        '''returns "It's perfect out there!" for temperature=75'''
       

class TestFizzBuzz:
    '''fizzbuzz() in control_flow.py'''

    def test_returns_fizzbuzz_multiple_3_and_5(self):
        '''returns "FizzBuzz" for num=0, num=15, num=45'''
       
    
    def test_returns_fizz_multiple_3_not_5(self):
        '''returns "Fizz" for num=3, num=33, num=42'''
        
    def test_returns_buzz_multiple_5_not_3(self):
        '''returns "Buzz" for num=5, num=10, num=50'''
       
    def test_returns_num_multiple_not_3_or_5(self):
        '''returns num for num=2, num=13, num=59'''
        

class TestCalculator:
    '''calculator() in control_flow.py'''

    def test_returns_sum_if_plus(self):
        '''returns sum for ("+", 1, 2), ("+", 5, 7), ("+", 9, 90)'''
        
    def test_returns_difference_if_minus(self):
        '''returns difference for ("-", 1, 2), ("-", 7, 5), ("-", 9, 9)'''
        
    def test_returns_product_if_times(self):
        '''returns product for ("*", 1, 2), ("*", 5, 7), ("*", 9, 10)'''
       
    def test_returns_quotient_if_divided_by(self):
        '''returns quotient for ("/", 1, 1), ("/", 14, 7), ("/", 90, 9)'''
       
    def test_prints_invalid_returns_none_if_invalid(self):
        '''prints "Invalid operation!" and returns None if operation invalid'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        assert(calculator('a', 1, 2) == None)
        sys.stdout = sys.__stdout__
      
