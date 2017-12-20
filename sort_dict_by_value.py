# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted_dict = sorted(xs.items(), key=lambda x: x[1])
print(sorted_dict)

# Alternately:
# import operator
# sorted(xs.items(), key=operator.itemgetter(1))
