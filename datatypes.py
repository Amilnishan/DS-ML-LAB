print("Data types\n")

list1=list(input("enter 3 fruits seperated by commas:").split(','))
print("list of fruits=",list1)

set1=set(input("\nenter 3 fruits seperated by comma:").split(','))
print("set of fruits=",set1)

tuple1=tuple(input("\nenter 3 fruits seperated by commas:").split(','))
print("tuple of fruits:",tuple1)

slno=input("\nenter 3 numbers ordered seperated by commas:").split(',')
fruit=input("enter 3 fruits sepertated by commas:").split(',')
dictonary={slno[0]:fruit[0],slno[1]:fruit[1],slno[2]:fruit[2]}
print("Dictonary=",dictonary)

#write a program to find the max number in a list

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

list4=list(input("enter 5 fruits separated by commas:").split(','))
print("list of fruits=",list4)
print("list without duplicates=",list(set(list4)))

tuple2=tuple(input("enter 3 fruits separated by commas:").split(','))
print("tuple of numbers:", tuple2)
dict2=dict(enumerate(tuple2, start=1))
print("Tuple to dictionary:", dict2)

dict1={1:'apple',2:'banana',3:'mango'}
dict2={4:'orange',5:'grape'}
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
dict1.update(dict2)
print("Merged Dictionary:", dict1)

#write a program that takes two lists and return true if they have at least one common member

list1 = list(map(int, input("Enter 5 numbers separated by commas for list1: ").split(',')))
list2 = list(map(int, input("Enter 5 numbers separated by commas for list2: ").split(',')))

def common_member(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False
print(common_member(list1, list2))