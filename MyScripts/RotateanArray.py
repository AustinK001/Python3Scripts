n = 3
list_1 = [1, 2, 3, 4, 5, 6]
list_1 = (list_1[len(list_1) - n:len(list_1)]+ list_1[0:len(list_1) - n])
print(list_1)

 #Print  = [4,5,6,1,2,3]
 #Rotated to the right

x = 5
list_2 = [1,2,3,4,5,6,7,8,9,10]
list_2 = (list_2[len(list_2) - x:len(list_2)]+ list_2[0:len(list_2) - x])
print(list_2)
# ^ (list_2[10 - 5:10] =

c = 2
list_3 = [1,2,3]
list_3 = (list_3[len(list_2) - c:len(list_3)]+ list_3[0:len(list_3) - c])
print(list_3)
# list_3[3 - 2:len] + list_3[0:len-2] Adding indexs together to join segments of the array
