def maxhouseRobber(hlist,currentHouse):
    if currentHouse >  len(hlist)-1:
        return 0 
    else:
        stealFirstHouse = hlist[currentHouse] + maxhouseRobber(hlist,currentHouse + 2)
        skipfirstHouse = maxhouseRobber(hlist,currentHouse + 1)
        return max(stealFirstHouse,skipfirstHouse)
    

alist = [6,7,1,30,8,2,4]
print(maxhouseRobber(alist,0))