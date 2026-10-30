a=int(input("Enter number of item="))
b=int(input("Enter price of item="))
c=a*b
print("Total amount=",c)
d=int(input("Enter discount="))
e=c*d/100
print("Discount=",e)
f=c-e
print("Paid ammount=",f)