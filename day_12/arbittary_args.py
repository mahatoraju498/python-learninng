#Arbitary arguments are like an expandable bucket which can accept any number of parameters.
# *args and **kwarggs are the arbitary argument in python


def addition(*args):
    print(args)  #it gives tuple
    return sum(args)


print(addition(1,2))
print(addition(1,2,3))
print(addition(1,2,3,4))
print(addition(1,2,3,4,5))



#**kwargs

def subtract(**kwargs):
    print(kwargs)#it gives dictionary
    return kwargs["a"]-kwargs["b"]


print(subtract( a=2, b=1))
print(subtract( a=10, b=2,c=1))
print(subtract(a=7, b=3,c=2,d=1))