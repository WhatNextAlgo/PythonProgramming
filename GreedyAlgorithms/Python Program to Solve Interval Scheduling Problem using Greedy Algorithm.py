def interval_scheduling(stimes,ftimes):
    index =  list(range(len(stimes)))
    index.sort(key= lambda x: ftimes[x])

    maximal_set = set()
    prev_finish_time = 0
    for i in index:
        if stimes[i] >= prev_finish_time:
            maximal_set.add(i)
            prev_finish_time = ftimes[i]
    return maximal_set


n = int(input('Enter number of activities: '))
stimes = input('Enter the start time of the {} activities in order: '
              .format(n)).split()
stimes = [int(st) for st in stimes]
ftimes = input('Enter the finish times of the {} activities in order: '
               .format(n)).split()
ftimes = [int(ft) for ft in ftimes]
 
ans = interval_scheduling(stimes, ftimes)
print('A maximum-size subset of activities that are mutually compatible is', ans)
