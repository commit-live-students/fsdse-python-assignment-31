import itertools


def solution(dic):
    list_of_combinations = []
    for k in itertools.product(*sorted(dic.values())):
        list_of_combinations.append(k[0]+k[1])
    return list_of_combinations

print(solution({'one':['a','b'], 'two':['c','d']}))
