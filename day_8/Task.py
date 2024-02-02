#Write a program which takes radius as an input and calculate the area of circle.pi*r**2


radius = int(input("enter the number"))
result = 22/7*radius**2
print(result)


#Write a program to find the frequency of the input number in a list 
#[5, 2, 3, 5, 3, 2, 3, 3, 1, 4]

data= [5, 2, 3, 5, 3, 2, 3, 3, 1, 4]
num = int(input("enter the number"))
count = data.count(num)
print(f"The frequency of {num} is {count}")