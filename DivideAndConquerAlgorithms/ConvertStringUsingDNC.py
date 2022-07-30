def findMinimumOpeartion(s1,s2,index1,index2):
    if index1 == len(s1):
        return len(s2) - index2
    
    if index2 ==len(s1):
        return len(s1) - index1

    if s1[index1] == s2[index2]:
        return findMinimumOpeartion(s1,s2,index1+1,index2+1)
    else:
        deleteop = 1 + findMinimumOpeartion(s1,s2,index1,index2 + 1)
        insertop = 1 + findMinimumOpeartion(s1,s2,index1 + 1,index2)
        replaceop = 1 + findMinimumOpeartion(s1,s2,index1+1,index2+1)

        return min(deleteop,insertop,replaceop)

s1 = "a"
s2 = "b"
print(findMinimumOpeartion(s1,s2,0,0))
