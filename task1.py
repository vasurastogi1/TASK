#TASK 1.1  LIST OPERATIONS :
 
my_list = [1,"vasu",2,"anshul",3,4]
my_list.append(5)
print("AFTER APPENDING : ", my_list)
my_list.remove(3)
print("AFTER REMOVING :",my_list)
my_list[1]= 10
print("AFTER UPDATING : ",my_list)




#TASK 1.2 DICTIONARIES OPERATIONS :             
my_dict = {"name":"vasu","program":"BCA","enroll_no":"TCA220"}
my_dict["gender"]="male"
print("AFTER ADDING :",my_dict)
del my_dict["program"]
print("AFTER REMOVING :",my_dict)
my_dict["enroll_no"]="TCA111"
print("AFTER UPDATING  :",my_dict)





#TASK 1.3 SET OPERATIONS
my_set = {"vasu","rastogi","bca"}
my_set.add("tca220")
print("AFTER ADDING :",my_set)
my_set.remove("bca")
print("AFTER REMOVING :",my_set)
my_set.discard("vasu")
my_set.add("VASU")
print("AFTER UPDATING :",my_set)
