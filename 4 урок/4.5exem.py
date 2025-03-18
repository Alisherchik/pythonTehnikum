numbers = [i for i in range (1,11)]
chot = [num for num in numbers if num % 2 == 0]
nechot = [num for num in numbers if num % 2 != 0]

print(chot, nechot)

chotnie = []
for i in numbers:
    if i % 2 == 0:
        chotnie.append(i)
        print(chotnie)
