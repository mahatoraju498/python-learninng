#lambd function are the short and elegant functions with one -liner statement
#They are mostly used in the cases where we do not need to call the function rather we hust need to pass the reference
#They are also called "anonymi=ous function" as they don't have their name



def is_even(num):
    return num % 2 == 0


x = lambda num: num % 2 == 0
print(x)