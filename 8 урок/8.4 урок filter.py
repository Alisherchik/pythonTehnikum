l = [1, 2, 3, 4, 5, 6]

a = list (filter(lambda x: x%2 == 0,l))
print(tuple(a))
print(a)


x = [1, 2, -4, -4, -8, -7, 4, 15, 18, 19, 21, -98]
y = list(filter(lambda a: a>0, x))
z = list(filter(lambda b: b'-', x))
print(y)
print(z)