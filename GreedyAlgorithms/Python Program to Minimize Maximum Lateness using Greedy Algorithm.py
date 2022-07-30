def minimize_lateness(ttimes,dtimes):
    index = list(range(len(ttimes)))
    index.sort(key = lambda x: dtimes[x])

    min_lateness = 0
    start_time = 0

    for x in index:
        min_lateness = max(min_lateness,(ttimes[x] + start_time) - dtimes[x])
        start_time += ttimes[x]

    return min_lateness , index


n = int(input('Enter number of requests: '))
ttimes = input('Enter the time taken to complete the {} request(s) in order: '
              .format(n)).split()
ttimes = [int(tt) for tt in ttimes]
dtimes = input('Enter the deadlines of the {} request(s) in order: '
               .format(n)).split()
dtimes = [int(dt) for dt in dtimes]
 
min_lateness, schedule = minimize_lateness(ttimes, dtimes)
print('The minimum maximum lateness:', min_lateness)
print('The order in which the requests should be scheduled:', schedule)