import itertools


def solution(dic):
    list_of_combinations = []
    onevalues=dic['one']
    twovalues=dic['two']
    for i in range(0,len(onevalues)):
        for j in range(0,len(twovalues)):
            list_of_combinations.append(onevalues[i]+twovalues[j])
    return list_of_combinations
print solution({'one':['a','b'], 'two':['c','d']})
