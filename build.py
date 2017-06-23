def solution(dic1):
    list_a = sorted(dic1.values())
    list_1 = list_a[0]
    list_2 = list_a[1]
    final_list=[]
    for i in range(len(list_a)):
        for j in range(len(list_a)):
            final_list.append(list_1[i]+list_2[j])
    return final_list
