#we can alter the flow of the loop in python using one of the followig statement
#1. Break 
#2.continue
#3.pass



# break
for each in [1,2,3,4,5,6,7]:
    print(each)
    if each == 4:
        break
else:
    print("The loop is executed completely")



a = 1
while a<10:
    print(a)
    if a == 4:
        break
    a+=1
print("The loop is executed completely")


# continue
# continue is used in the sense of skipping the loop
for each in [1,2,3,4,5,6,7]:
    if each == 4:
        continue
    print(each)



a = 1
while a<10:
    if a == 4:
        a+=1
        continue
    print(a)
    a+=1

# pass
# pass is used if we want to add codes in future but we want it syntatically correct at the moment