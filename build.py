import itertools


def solution(dic):
    list_of_combinations = []
    '''
    Enter your code here
    '''
    dic1 = dic['one']
    dic2 = dic['two']
    list_of_combinations = [dic1[i] + dic2[j] for i in range(len(dic1)) for j in range(len(dic2))]
    return list_of_combinations
