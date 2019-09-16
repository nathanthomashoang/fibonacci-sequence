# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:42:54 2019

@author: Nathan Hoang
"""

def recursive_fibo(num):
    '''function to return fibonacci value'''
    if num <= 1:
        return num
    return recursive_fibo(num-2) + recursive_fibo(num-1)

def shell():
    '''to run program'''
    while True:
        try:
            term = int(input('Up to how many terms to return fibonacci?: '))
        except ValueError:
            print('\nPlease only input an integer.')
        else:
            if term <= 0:
                print("\nPlease enter a positive integer")
            else:
                break
    print("\nFibonacci sequence:\n")
    for num in range(term + 1):
        print(recursive_fibo(num))

shell()
