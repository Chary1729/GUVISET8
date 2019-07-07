num1,num2=map(int,input().split())
prod=num1*num2
for i in range(0,prod+1):
 if(i**2==num1*num2):
  print("yes")
  break
else:
  print("no")
  
