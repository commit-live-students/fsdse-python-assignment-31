import itertools

dictn = {'one':['a','b'], 'two':['c','d']}

def solution(dic):
    li = []
    key_list = dic.values()

    for i in range(0, 2):
        for j in range(0, 2):
            x = key_list[1][i] + key_list[0][j]
            li.append(x)
    print li
    return li

solution(dictn)
