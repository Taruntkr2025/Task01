#age=18 print adult
#age>12 print teenage
#age<12 print kid

age=int(input("Enter age "))

if age>18:
    print("your are Adult or Major")
elif 12 < age <=18:
    print("your are Teenager")
else:
    print("Kid")