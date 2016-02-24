''' Given two string check if one string is permutation of other'''

def permutation(str1,str2):
    sort_str1 = sorted(str1)
    sort_str2 = sorted(str2)
    if len(sort_str1) != len(sort_str2):
        return False
    for index in range(len(sort_str1)):
       if sort_str1[index] == sort_str2[index]:
           index = index + 1
       else:
           return False
    return True


print(permutation('doa','god'))





