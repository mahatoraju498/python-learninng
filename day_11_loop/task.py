# WAP to delete all the occurrences of a specified character in a given string
# S = “All the occurrences of a specified character in a given string”
# Input = “a”
# Output = “ll occurrences of  specified chrcter in  given string”



s = "All the occurrences of a specified character in a given string"
result = ""
char = input("enter a character")
for each in s:
    if each.lower()==char.lower():
        continue
    result+= each
print(result)



#Create a new list of repeated items from a provided list:
#nums = [3, 4, 2, 2, 1, 3, 3, 3]
#Output = [3, 2]



nums = [3,4,2,2,1,3,3,3]
num1 = []
for each in nums:
    if nums.count(each)>1 and each not in num1:
        num1.append(each)
print(num1)
    