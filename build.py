import itertools


def solution(dic):
    list_of_combinations = []
    '''
    Enter your code here
    '''
    # Question needs to be corrected
    for element1 in dic['one']:
        for element2 in dic['two']:
            list_of_combinations.append(element1+element2)
    return list_of_combinations
