s=input("Enter any string:")
l=s.split()
#for i in l:
    #length=len(l)
print(l)
print("palidrom sting  {}".format(s))
if(s==s[::-1]):
    print("This is a palidrom")
else:
    print("This is not a palidrom")
