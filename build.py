import itertools, operator

def solution(dic):
    list_of_combinations = []
    '''
    Enter your code here
    '''
    letter_groups = list(sorted(dic.values()))
    for i in range(len(letter_groups)-1):
        for j in range(i+1, len(letter_groups)):
            l1, l2 = letter_groups[i], letter_groups[j]
            g = [list(zip(x, l2)) for x in list(itertools.permutations(l1, len(l2)))]
            pairs = list(set(['{}{}'.format(x[0],x[1]) for x in reduce(operator.concat, g)]))
            list_of_combinations.append(pairs)
    list_of_combinations = sorted(reduce(operator.concat, list_of_combinations))
    return list_of_combinations

d = {'one':['a','b'], 'two':['c','d']}
print(solution(d))
