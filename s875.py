#hel*lo
k=input()
l=len(k)
if(l%2!=0):
  k=k[:l//2]+'*'+k[(l//2)+1:l]
  print(k)
else:
  k=k[:(l//2)-1]+'**'+k[(l//2)+1:l]
  print(k)
  
