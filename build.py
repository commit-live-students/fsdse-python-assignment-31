import itertools


def solution(dic):
    list_of_combinations = []
    for combo in itertools.product(*[dic[k] for k in sorted(dic.keys())]):
        list_of_combinations.append(''.join(combo))
    print list_of_combinations
    return list_of_combinations
#dic = {'one': ['a', 'b'], 'two': ['c', 'd']}
#solution(dic)
