# def is_even(num):
#     return num %2 == 0

# num = int(input("enter the number"))
# result = is_even(num)
# print(result)



data = [2, 3, 4, 5, 6]



    


result = map(lambda e:e** 2, data)
print(list(result))   # [4, 9, 16, 25, 36]

data = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

vowel_data = filter (lambda element: element in ["a", "e", "i", "o", "u"] , data)
print(list(vowel_data))


from functools import reduce

data = [1, 2, 3, 4, 5]

result = reduce(lambda element1,element2: element1 * element2, data)
print(result)