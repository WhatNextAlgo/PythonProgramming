a=[[1,[[2]],[[[3]]]],[[4],5]]

flatten = lambda l: sum(map(flatten,l),[]) if isinstance(l,list) else [l]

print(flatten(a))