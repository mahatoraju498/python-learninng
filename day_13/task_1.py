#Wap to calculate the factorial of 7 using python reduce() function eith lambda

from functools import reduce




result=(reduce(lambda element1, el2 : element1 *el2 ,range(1,8)))
print(result)
