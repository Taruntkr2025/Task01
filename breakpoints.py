#  write a simple python program print 1 to 50 numbers skip 10 20 30 40 50
# 10,20,30,40,50
"""
for num in range(1,50):
    if num in [10,20,30,40,50]:
        continue
    print(num,end=" ,")
    """
    

#try catch

"""

num1=int(input("Please enter num1:"))
num2=int(input("Please enter num2:"))

def div(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError as e:
        return e
    finally:
        print("Execution is complete")

print (div(num1, num2))
"""

#list even numbers from range 1-21

li_even=[]

for i in  range(1,21):
    if i%2==0:
        li_even.append(i)
print(li_even)

    