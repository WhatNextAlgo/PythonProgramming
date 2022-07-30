def Lps(s,startindex,endindex):
    if startindex > endindex:
        return 0
    elif startindex == endindex: # middle elem
        return 1
    elif s[startindex] == s[endindex]:
        return 2 + Lps(s,startindex + 1, endindex -1)
    else:
        op1 = Lps(s,startindex, endindex-1)
        op2 = Lps(s,startindex+1, endindex)
        return max(op1,op2)



s = "abccccdd"
print(Lps(s,0,len(s)-1))