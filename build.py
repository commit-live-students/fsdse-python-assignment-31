def solution(dic):
    list_of_combinations = []
    a_list = [c for c in dic['one']]
    b_list = [c for c in dic['two']]
    for a in a_list:
        for b in b_list:
            list_of_combinations.append(a + b)
    return list_of_combinations
