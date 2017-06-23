import itertools


def solution(dic):
    list_of_combinations = []
    '''
    Enter your code here
    '''
    l=[]
    for i in range(2):
        for j in range(2):
            l.append([dic['one'][i],dic['two'][j]])
    for var in l:
        list_of_combinations.append(''.join(var))
    return list_of_combinations
