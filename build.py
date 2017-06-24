import itertools


def solution(dic):
    list_of_combinations = []
    dict1 = dic['one']
    dict2 = dic['two']
    list_of_combinations = [dict1[i]+dict2[j] for i in range(0,len(dict1)) for j in range (0,len(dict2))]
    return list_of_combinations

# solution({'one':['a','b'], 'two':['c','d']})
# Output: ['ac', 'ad', 'bc', 'bd']
