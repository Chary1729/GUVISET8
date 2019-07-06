arr=[]
myinput=int(input())
for i in range(1,myinput+1):
  if(myinput%i==0):
    arr.append(i)
print(*arr)
