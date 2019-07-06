inputs=input()
vow=['a','e','i','o','u']
x=any(c in inputs for c in vow)
if(x==True):
  print('yes')
else:
  print('no')
