import itertools
def solution(dic):
    combinations = []
    dic1 = dic['one']
    dic2 = dic['two']
    combinations = [dic1[i]+dic2[j] for i in range(0,len(dic1)) for j in range (0,len(dic2))]
    return combinations
