import itertools

input_dic = {'one':['a','b'], 'two':['c','d']}

def solution(dic):
    list_of_combinations = []
    '''
    Enter your code here
    '''
    string_1 = ""
    string_2 = ""
    for i in dic['one']:
        string_1 += i
    for j in dic['two']:
        string_2 += j

    for i in string_1:
        for j in string_2:
            list_of_combinations.append(i+j)

    print list_of_combinations

    return list_of_combinations

solution(input_dic)
