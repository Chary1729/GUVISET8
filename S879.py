nums1,num2=map(int,input().split())
prod=nums1*num2
for k in range(0,prod+1):
 if(k**2==nums1*num2):
  print("yes")
  break
else:
  print("no")
  
