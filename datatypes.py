print("Data types\n")

"""list1=list(input("enter 3 fruits seperated by commas:").split(','))
print("list of fruits=",list1)

set1=set(input("\nenter 3 fruits seperated by comma:").split(','))
print("set of fruits=",set1)

tuple1=tuple(input("\nenter 3 fruits seperated by commas:").split(','))
print("tuple of fruits:",tuple1)

slno=input("\nenter 3 numbers ordered seperated by commas:").split(',')
fruit=input("enter 3 fruits sepertated by commas:").split(',')
dictonary={slno[0]:fruit[0],slno[1]:fruit[1],slno[2]:fruit[2]}
print("Dictonary=",dictonary)"""

list2=list(input("\nenter 5 numbers seperated by commas:").split(','))
print("list of numbers=",list2)
print("Max number in the list is:",max(list2))

list3=list(map(int, input("\nenter 5 numbers seperated by commas:").split(',')))
print("list of numbers=",list3)
max = list3[0]
for i in list3:
    if i > max:
        max = i
print("Max number in the list is:", max)