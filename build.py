import itertools


def solution(dic):
    list_of_combinations = []
    '''
    Enter your code here
    '''
    all_elements = []

    for key in dic:
        elements = dic[key]
        all_elements.append(elements)

    for i in range (0, len(all_elements)):
        a = all_elements[i]
        for j in range (0, len(a)):
            c = all_elements[1][i] + all_elements[0][j]
            list_of_combinations.append(c)

    return list_of_combinations


'''
dic = {'one': ['a', 'b'], 'two': ['c', 'd']}
a = solution(dic)
print a
'''
