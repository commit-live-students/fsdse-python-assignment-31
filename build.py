import itertools


def solution(dic):
    list_of_combinations = []
    '''
    Enter your code here

    '''
    values = [v[1] for v in sorted(dic.items())]
    list_of_combinations = ["".join(x) for x in itertools.product(*values)]
    # for i in dic['one']:
    #     for j in dic['two']:
    #         list_of_combinations.append(i+j)

    return list_of_combinations

dic = {'one':['a','b'], 'two':['c','d']}
print(solution(dic))
