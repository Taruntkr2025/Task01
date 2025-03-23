#write a lambda expression to add two numbers
"""
addTwoNumbers = lambda a, b: a+b
print(addTwoNumbers(12,8))"
"""

"""
my_num=int(input("enter a number"))
is_even=lambda a: a%2==0
print(is_even(my_num))
"""
"""
my_list=[1,2,3,4,5]

squareRoots=list(map(lambda x:x**2,my_list))
print(squareRoots)
"""
#FILTER

""""
my_values=["Hello,World","Good Morning"]
split_values=list(map(lambda x:x.split(" "),my_values))
print(split_values) 
"""

my_values=[1,2,3,4,5,6,7,8,9,10]
odd_nums=list(filter(lambda x:x%2!=0,my_values))
print(odd_nums)