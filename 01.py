name= input("give me your name: ")

age= int(input("how old are you: "))

year= 2022 - age + 100

print(name, "you will be 100 years old in the year " + str(year))

num= int(input("give me a number to check "))
check= int(input("give me a number to divide "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "doesn't evenly by", check)

a1=[1, 2, 3, 4, 5 ,6, 7]
a= [ a1[x] for x in (0, -1) ]
print(a)

age = int(input("how old are you ? "))
if age >= 18:
    print('you can drive')
elif age < 18:
    print('you can not drive')
else:
    print( )

x = open('C:/Users/ADMIN/Desktop/manhcuong/manhcuong.txt', 'w')
x.write('lemanhcuong')
x.close()

x= open('C:/Users/ADMIN/Desktop/manhcuong/manhcuong.txt', 'r')
print(x.read())


def max_of_three(a,b,c):
    max_3= 0
    if a > c:
        max_3= c
    else:
        max_3= a

    if b > c:
        max_3 = b
    else:
        max_3 = c
    return max_3
max_of_three(1,2,3)


number = 17
print(f"The number is {number + 3}")

import datetime
current_year= datetime.datetime.now().year
name= input("what is your name ? ")
age= int(input("How old are you ? "))
print ( f"{name}, you will be 100 years old in { current_year - age + 100}" )
