def last(n): return n[-1]

def sortinglist(tuples):
  return sorted(tuples, key=last)

print(sortinglist([(5, 1), (1, 5), (0, 6), (1, 5)]))
