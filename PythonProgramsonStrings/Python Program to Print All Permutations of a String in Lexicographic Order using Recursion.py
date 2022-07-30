from math import factorial

def print_permutations_lexicographic_order(s):
    seq = list(s)

    for _ in range(factorial(len(seq))):

        print("".join(seq))

        nxt = get_next_permutation(seq)
        print("Nxt in for : ",nxt)

        # if seq is the highest permutation
        if nxt is None:
            # then reverse it
            seq.reverse()
        else:
            seq = nxt

count = 0
def get_next_permutation(seq):
    """Return next greater lexicographic permutation. Return None if cannot.
 
    This will return the next greater permutation of seq in lexicographic
    order. If seq is the highest permutation then this will return None.
 
    seq is a list.
    """

    if len(seq) == 0:
        return None

    print("Seq : ",seq)
    print("Seq : ",seq[1:])
    nxt = get_next_permutation(seq[1:])

    print("nxt : ",nxt)

    if nxt is None:
        print("seq[1:] : ",seq[1:])
        print("reversed(seq[1:]) : ",reversed(seq[1:]))
        # reverse seq[1:], so that seq[1:] now is in ascending order
        seq[1:] = reversed(seq[1:])
        print("after reversed seq: ",seq)
        print("after reversed: ",seq[1:])

     # find q such that seq[q] is the smallest element in seq[1:] such that
        # seq[q] > seq[0]
        q = 1
        while q < len(seq) and seq[0] > seq[q]:
            q += 1

        # if cannot find q, then seq is the highest permutation
        if q == len(seq):
            print("q:",q , "seq :",seq , len(seq))
            return None


        # swap seq[0] and seq[q]
        seq[0], seq[q] = seq[q], seq[0]
        print("Before Return when nxt is None: ",seq)
 
        return seq
    else:
        print("[seq[0]] + nxt :",[seq[0]] + nxt)
        return [seq[0]] + nxt

        
#s = input('Enter the string: ')
#print_permutations_lexicographic_order(s)


def permutations1(remaining, candidate=''):
     
    if len(remaining) == 0:
        print(candidate)
 
    for i in range(len(remaining)):
        print("candidate: ",candidate , "Rem : ",remaining, "index: ",i)
        newCandidate = candidate + remaining[i]
        print("newCandidate",newCandidate)
        newRemaining = remaining[0:i] + remaining[i+1:]
        print("newRemaining",newRemaining)
 
        permutations(newRemaining, newCandidate)
 

def permutations(s):
    
    # base case
    if not s:
        return []

    # create a list to store (partial) permutations
    partial = []

    # initialize the list with the first character of the string
    partial.append(s[0])

    # do for every character of the specified string
    for i in range(1, len(s)):

        # consider previously constructed partial permutation one by one

        # iterate backward
        for j in reversed(range(len(partial))):

            # remove the current partial permutation from the list
            print("partail: ",partial,"j: ",j)
            curr = partial.pop(j)
            print("curr: ",curr)

            # Insert the next character of the specified string into all
            # possible positions of current partial permutation.
            # Then insert each of these newly constructed strings into the list

            for k in range(len(curr) + 1):
                partial.append(curr[:k] + s[i] + curr[k:])

    print(partial, end='')
 
 

 
if __name__ == '__main__':
 
    s = 'ABC'
    permutations(s)



