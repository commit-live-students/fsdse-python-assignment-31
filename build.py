import itertools


def solution(dic):
    list_of_combinations=[]
    for combo in itertools.product(*[dic[k] for k in sorted(dic.keys())]):
        list_of_combinations.append(combo)
    return [''.join(t) for t in list_of_combinations]
