#sorting: arranging the items in a given pattern is called sorting.
#[1,3,2,4,1]
# ascending [1,1,2,3,4]
# descending [4,3,2,1,1]
#why do we need to sort? 
#to decrease the time of compution
#searching
#[1,2,3,4,1,2,4,2,5,6,3,7,8,3]: linear searching
#traversed
#linear searching: It is a searching algorithm in which we traverse each element one-by-one.
#it is not advisable because of time issues.
#binary searching: it only works on sorted arrays.
#[1,1,2,3,4,5,6,7,8,9]
#[5,6,7,8,9]
#[7,8,9]
#[8,9]
#[12,13,14,16,22,29,37,42,48] number to find: 13
#[12,13,14,16,22]
#[12,13,14]
#linear search
# li = [1,3,4,2,5,1,5,1,5,7,5,3]
# a = int(3)#number which we have to find
# counter = int(0) 
# for i in li: 
#     if i == a:
#         counter = counter+1
#         break
# if(counter):
#     print("number found")
# else:
#     print("number not found")