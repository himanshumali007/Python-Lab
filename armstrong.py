def Arm(x) 
   t=x
   sum1=0
   while(t>0):
     d=t%10
     sum1+=d**3
     t=t//10
   if sum1==x:
     print('A')
   else:
     print('NA')
x=int(input())
Arm(x)
