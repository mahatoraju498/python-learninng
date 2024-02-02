#loops can be used in the datatypes which are itreables
#Iterable datatypes are list ,string, tuple,set,dictionary


#Looping in a list


vowels = ["a","e","i","o","u"]
for each in vowels:
    print(each) # a e i o u

#looping in a tuple
vowels = ("a","e","i","o","u")
for each in vowels:
    print(each) # a e i o u


#looping in a stirng
data = "hello world, i am learing python"
for each in data:
    print(each)



#looping in a dictionary

student = {"name":"Raju", "email":"r@eamil.com","address":"ktm"}
for each in student:
    print(each)#name email adress


print(student.values())  # dict_values(["Raju", "r@email.com", "KTM"])
for each in student.values():   
    print(each)  # Raju  r@email.com  KTM
    

for each in student.keys():   
    print(each)  # name  email  address


print(student.items())  # dict_items([("name", "Raju), ("email", "r@email.com"), ("address", "KTM")])
for each in student.items():
    print(each)  # ("name", "Raju")   ("email", "r@email.com")   ("address", "KTM")
 
for key, value in student.items():
    print(key)  # "name"  "email"  "address"
    print(value)  # "Raju"  "r@email.com"  "KTM"



#we can use "else" with loop in python

data = ["a","e","i","o","u"]
for each in data:
    print(each)#a e i o u


else:
    print("This block runs if the iteration is done completely")


    