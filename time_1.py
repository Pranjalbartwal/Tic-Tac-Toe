s=int(input("Enter time in seconds="))
m=int(s/60)
s=s%60
h=int(m/60)
m=m%60
print(h,":",m,":",s)