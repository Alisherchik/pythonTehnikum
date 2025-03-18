a = [1, 2, 3, 4, 5, 6]
b = ['Oleg', 'Igor', 'Ivan', 'Volodya']
c = [3.1, 5.6, 54.0, 0.5]

a1 = [i+5 for i in a]
print(a1)

b1 = [i+'5' for i in b]
print(b1)

c1 = [i+2.5 for i in c]
print(c1)

numbers = [i for i in range(1, 21)]
num1 = [num for num in numbers if num % 2 == 0]
num2 = [num for num in numbers if num % 2 != 0]

print(num2)

nums1 = [num for num in range(1, 21)]
nums2 = [num for num in nums1 if num % 2 == 0]
print(nums2)