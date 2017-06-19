"""
Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
Notes:

Define a function which will accept a dict parameter.
For all present keys it will fetch values and will create a pair as described in above example.
Store it in list and return.
Instructions:

Program should be written in file build.py

Function name should be solution.
Input
 Type:  Dictionary
 Value: {'one':['a','b'], 'two':['c','d']}
Expected Output
  Type:  List
  Value: [ac, ad, bc, bd]
"""
import itertools
def solution(dic):
    list_of_combinations = []
    dic1 = dic['one']
    dic2 = dic['two']
    list_of_combinations = [dic1[i]+dic2[j] for i in range(0,len(dic1)) for j in range (0,len(dic2))]
    return list_of_combinations
