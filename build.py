import itertools

list_of_combinations = {}
def solution(dic):
    print sorted(dic.keys())
    print type(sorted(dic.keys()))

    values = [v[1] for v in sorted(dic.items())]
    list_of_combinations = [''.join(x) for x in itertools.product(*values)]

    return list_of_combinations

print solution({'one':['a','b'], 'two':['c','d']})
