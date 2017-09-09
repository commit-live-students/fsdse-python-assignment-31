import itertools


def solution(dic):
    list_of_combinations = []
    for combo in itertools.product(*[dic[k] for k in sorted(dic.keys())]):
        list_of_combinations.append(''.join(combo))
    return list_of_combinations
