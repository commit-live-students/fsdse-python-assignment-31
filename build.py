import itertools

dic={'one':['a','b'], 'two':['c','d']}

def solution(dic):
    list_of_combinations = []
    for x in itertools.product(*[dic[k] for k in sorted(dic.keys())]):
        #print(''.join(x))
        list_of_combinations.append(''.join(x))
    return list_of_combinations

output=solution(dic)
print output
