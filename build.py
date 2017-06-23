def solution(dic):
    list_of_combinations = []
    list_values = []
    # sortd_strng = []
    string_values = []
    concat_string = []
    for key in dic:
        list_values.append(dic[key])
    #print list_values
    for elem in list_values:
        for sub_elem in elem:
            string_values.append(sub_elem)

    sortd_strng = sorted(string_values)
    # print sortd_strng
    for i in sortd_strng[:2]:
        for j in sortd_strng[2:4]:
            val = "".join(i + j)
            list_of_combinations.append(val)
        # print concat_string
    return list_of_combinations
