#list comprehension is a short elegant way to create a list in one line

data = [1,2,3,4,5,6,]
result = []
for each in data:
    result.append(each*3)

print(result) #[3,6,9,12,15,18]



result = [each*3 for each in data]  #list comprehension
print(result)  #[3,6,9,12,15,18]


#We can also use if condition in comprehension

result = [each*3 for each in data if (each*3) % 2 == 0]
print(result) #Gives only the even result



#Create a list of even numbers in range 0 t 50 using comprehension

result = [ each for each in range(0,51) if each % 2 ==0]
print(result)


#like list comprehension we also have dictionary comprehension in python

result = { key:value for key,value in [("name","john")("age","30")("adress","ktm")]}
print(result)#{'name}


result = {i: i*2 for i in range(1,10)}
print(result) #      