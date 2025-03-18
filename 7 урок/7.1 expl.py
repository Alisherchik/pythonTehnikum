def spam1(*args):
    for i in args:
        print(i)
    return args
print(spam1(1,2,3,'Hello'))