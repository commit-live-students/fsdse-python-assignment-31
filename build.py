import itertools


def solution(dic):
    lst = []
    tmp = dic.values()
    tmp.sort()
    print tmp
    tmp2 = []
    k = 0
    print tmp
    for i in range(len(tmp)):
        for k in range(len(tmp)):
            lst.append(tmp[0][i]+tmp[1][k])
    print lst
    return lst

solution({'one':['a','b'],'two':['c','d']})
