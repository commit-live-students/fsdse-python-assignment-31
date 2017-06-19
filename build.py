import itertools

def solution(dic):
    list2 = list(''.join(v) for k,v in dic.items())
    #list1 = list(itertools.product('ab','cd'))
    print(list2.reverse())
    list1 = list(itertools.product(*list2))
    '''
    Enter your code here
    '''
    #print(list1)
    list_of_combinations = [x[0]+x[1] for x in list1]
    return list_of_combinations
#print(solution({'one':['a','b'], 'two':['c','d']}))
