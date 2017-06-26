import itertools


def solution(dic):
    list_of_combinations = []
    for combo in itertools.product(*[dic[k] for k in sorted(dic.keys())]):
        val = (''.join(combo))
        list_of_combinations.append(val)
    return list_of_combinations

my_dict = {'1':['a','b'], '2':['c','d']}
solution(my_dict)
