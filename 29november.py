#searching
#directly : google windows explorer
#superficial : 
# a = int(90)
# print(a)  #90
# li = [1,2,3,4,5,6,7,8,9,10,11,12]
#yes, I found the number 6 at index 5
# li = [2,1,5,2,6,3,9,4]
#I will use a for loop and traverse the list or the array and check for the specified element
# a = int(12)
# for i in range(len(li)):
#     if a==li[i]:
#         print("number is present in the list")
#         break
#     else:
#         print("number is not present in the list")

#space
#time
#best time complexity : shortest time
#worst time complexity : longest time
#average time complexity : medium time

#write a program to check for a particular element in the list. If the number is present then return the index else return the message "number is not present".

li = [1,2,3,4,5,6,7,8,9,10,11,12,13]
index = int(-1)
a = int(4)

for i in range(len(li)):
    if a == li[i]:
        index = i
        break

if index == -1:
    print("number not found")
else:
    print("number found at index",index)