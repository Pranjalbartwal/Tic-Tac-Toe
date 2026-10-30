d=int(input("enter number of days="))
y=int(d/365)
d=d%365
m=int(d/30)
d=d%30
w=int(d/7)
d=d%7
print("Year=",y)
print("Month=",m)
print("Week=",w)
print("Days=",d)