#python

#Range

#range(1,10)

#for i in range(1,10,2):
 #   print(i)
"""
even_numbers = []
odd_numbers = []

for num in range(1, 101):  
    if num % 2 == 0:
        even_numbers.append(num)  
    else:
        odd_numbers.append(num)   

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)"
"
"""

#Using While loop
"""
even_numbers = []
odd_numbers = []

num=1

while num <= 100:
    if num % 2 == 0:
        even_numbers.append(num) 
    else:
        odd_numbers.append(num)   
    num+=1
print("EVEN_Number are",even_numbers)
print("ODD_Numbers are",odd_numbers)"
"""

# 2*1=2
# 2*10=20

#f-String

num = 1  # Initialize counter

while num <= 10:  # Loop from 1 to 10
    print(f"2 * {num} = {2 * num}")  # Print multiplication result
    num += 1  
