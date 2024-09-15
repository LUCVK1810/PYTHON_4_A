#print list after removing the 0th, 2nd, 4th and 5th elements. 
l1=[1,2,3,4,5,6,7,8,9,0] 
print("Original List is",l1)  
print("According to question we have to remove 0th->1,2nd->3,4th->5,5th->6") 
l1.remove(l1[0]) #this line will remove 1 from the list, Therefore l1[0]=2 
print("After Removal of 0th element Now List is",l1) 
print("Now we have to remove 3 from list which is at 1th position of index") 
l1.remove(l1[1]) 
print("After Removal of 1st element of New List (original 2nd index element) is",l1) 
print("Now we have to remove 5 from list which is at 2nd position of index") 
l1.remove(l1[2]) 
print("After Removal of 3rd element of New List (original 4th index element) is",l1) 
print("Now we have to remove 6 from list which is at 2nd position of index") 
l1.remove(l1[2]) 
print (l1)
