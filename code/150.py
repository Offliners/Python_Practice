# using the "map" built-in function

data = [1,3,5,7,9]

def f(x):
    return x ** 2

# now use the f() function to
# compute the squares of all items

squares = map(f,data)
print(type(squares)) # it's a "map"

# convert it to a list
print(list(squares))

# Output:
# <class 'map'>
# [1, 9, 25, 49, 81]
