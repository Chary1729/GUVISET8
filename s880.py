inputs=input()
arr=[]
if(inputs.isdigit()==True):
  for i in inputs:
    if(int(i)%2!=0):
      arr.append(i)
print(*arr)
