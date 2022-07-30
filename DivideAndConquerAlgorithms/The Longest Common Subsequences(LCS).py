def lcs(s1,s2,index1,index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    elif s1[index1] == s2[index2]:
        return 1 + lcs(s1,s2,index1 + 1,index2 + 1)
    else:
        opt1 = lcs(s1,s2,index1 + 1,index2)
        opt2 = lcs(s1,s2,index1, index2 + 1)
        return max(opt1,opt2)



print(lcs("elephant","erepant",0,0))