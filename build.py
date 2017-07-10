import itertools


def solution(dic):
    list_of_combinations = []
    combinations = []
    dict1 = dic['one']
    dict2 = dic['two']
    combinations = [dict1[i]+dict2[j] for i in range(0,len(dict1)) for j in range (0,len(dict2))]
    return combinations
solution({'one':['a','b'], 'two':['c','d']})
