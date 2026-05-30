n=int(input("Enter the no of numbers in the list:"))
list1=[]
new_list=[]
for i in range(n):
    num=int(input("Enter the number:"))
    list1.append(num)
for items in list1:
    for j in range(2,items):
        if items % j==0:
            new_list.append(items)
            break
if new_list==list1:
    print("True")
else:
    print("False")
