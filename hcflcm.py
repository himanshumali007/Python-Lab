a=int(input())
b=int(input())
c=min(a,b)
for i in range(1,c+1):
  if ((a%i==0) and (b%i==0)):
   hcf=i
print("hcf:",hcf)

lcm=(a*b)/hcf
print("lcm:",lcm)
