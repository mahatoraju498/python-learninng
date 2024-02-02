#order of argument in python function is:
#1.Positional 
#2.Defult/Keyword
#3.*args
#4.**kwargs



def addition(a,b,c, d=2, e=3, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(args)
    print(kwargs)


adddition(10,20,5,9,12,3,7,8,9, x=14, y=13)