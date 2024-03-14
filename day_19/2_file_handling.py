#
#There are several modes in which we can open a file
#1.Read Mode(r)
#2.Write Mode(w)
#3.Append Mode(a)
#4.Read and write(r+)
#5.Write and read(w+)
#Append and Read (a+)
#Exclusive Write(x)




fp = open ("day_19/message.txt","w")
fp.write("helllo i am learinig file handling")
fp.close()
print("open")

fp = open("message.txt", "w")
try:
    fp.write("Hello I am learning file")
except:
    print("Something Went Wrong")
else:
    print("Successful !!")
finally:
    fp.close()

# If we open file in write mode then it overrides the previous content