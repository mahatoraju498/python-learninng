# try:
#     num = int(input("enter the number"))
#     num1 = int(input("enter the number"))
#     result = num / num1
#     print(result)
# except:
#     print("not divisible by zero")
    

try:
    num = int(input("enter the number"))
    num1 = int(input("enter the number"))
    result = num / num1
    print(result)
except Exception as e:

    print(e)
    