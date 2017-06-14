import itertools


def solution(dic):
    list_of_combinations = []
    '''
    Enter your code here
    '''
    my_list = []
    for key in dic:
        my_list.append(dic[key])

    my_list.reverse()
    return [''.join(w) for w in list(itertools.product(*my_list))]
