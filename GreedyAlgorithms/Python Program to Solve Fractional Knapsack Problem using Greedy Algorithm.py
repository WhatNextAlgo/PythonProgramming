def fractional_knapsack(value,weight,capacity):
    index = list(range(len(value)))
    print("list of index: ",index)

    ratio = [v/w for v,w in zip(value,weight)]
     # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key = lambda x : ratio[x],reverse=True)

    max_value = 0
    fractions = [0] * len(value)
    for x in index:
        if weight[x] <= capacity:
            fractions[x] = 1 
            max_value += value[x]
            capacity -= weight[x]
        else:
            fractions[x] = capacity/weight[x]
            max_value += value[x] * (capacity/weight[x])
            break

    return max_value,fractions

n = int(input('Enter number of items: '))
value = input('Enter the values of the {} item(s) in order: '
              .format(n)).split()
value = [int(v) for v in value]
weight = input('Enter the positive weights of the {} item(s) in order: '
               .format(n)).split()
weight = [int(w) for w in weight]
capacity = int(input('Enter maximum weight: '))
 
max_value, fractions = fractional_knapsack(value, weight, capacity)
print('The maximum value of items that can be carried:', max_value)
print('The fractions in which the items should be taken:', fractions) 


