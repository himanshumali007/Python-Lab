p=int(input("Enter element of row1 :"))
q=int(input("Enter element of column1 :"))
r=int(input("Enter element of row2 :"))
s=int(input("Enter element of column2 :"))
x=(p+q)%2
y=(r+s)%2
if (x==y):
    print("They are of same colour")
else:
    print("They are not of same colour")
