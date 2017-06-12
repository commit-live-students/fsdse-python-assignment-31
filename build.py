import itertools

dic={'one':['a','b'], 'two':['c','d']}

def solution(dic):
    list_of_combinations = []
    string_1 = ""
    string_2 = ""

    for i in dic['one']:
        string_1 += i
        print string_1
    for j in dic['two']:
        string_2 += j
        print string_2
    for i in string_1:
        for j in string_2:
            list_of_combinations.append(i+j)
    print list_of_combinations
    return list_of_combinations

solution(dic)
