def overlapping (list1,list2):
    for element in list1:
        if element in list2: 
            return True
    return False

list1 =input("enter the element in the list1 seprated by comma:").split(",")
list2 = input("enter the element in the list2 seprated by comma:").split(",")

result = overlapping(list1,list2)

print("does the overlapping result in list:",result)
