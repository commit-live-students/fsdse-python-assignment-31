import itertools

def solution(dic):
    '''
    Enter your code here
    '''
    result = []
    combinations = []
    combinations = list(itertools.product(*dic.values()))
    for i in combinations:
        if i[0] < i[1]:
            temp = i[0]+i[1]
            result.append(temp)
        else:
            temp = i[1]+i[0]
            result.append(temp)
    return sorted(result)
