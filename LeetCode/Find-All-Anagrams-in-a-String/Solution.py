    len_string_test =len(p)
    list_start = []

    for i in range(len(s)):
        list_test =s[i:i+len_string_test]
        if isAnag(list_test,p):
            list_start.append(i)

    return list_start
    