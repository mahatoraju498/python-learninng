# def is_even(num):
#     return num %2 == 0

# num = int(input("enter the number"))
# result = is_even(num)
# print(result)



# data = [2, 3, 4, 5, 6]



    
#reference form the lambda  topic

# result = map(lambda e:e** 2, data)
# print(list(result))   # [4, 9, 16, 25, 36]

# data = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

# vowel_data = filter (lambda element: element in ["a", "e", "i", "o", "u"] , data)
# print(list(vowel_data))


# from functools import reduce

# data = [1, 2, 3, 4, 5]

# result = reduce(lambda element1,element2: element1 * element2, data)
# print(result)


class Person:
    def __init__(self,name , age,address):
        self.name = name   #public 
        self._age = age #protected 
        self.__address = address #private
    
    def get_details(self):
        return(f"the name is {self.name}  and the age is {self._age} and the address is {self.__address}")
    

p1 = Person("Raju", 22, "ktm")
print(p1.name)
print(p1._age)
# print(p1.__address) #gives error as this is private
print(p1.get_details())