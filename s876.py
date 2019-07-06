myinputs=int(input())
temp=myinputs
if(myinputs==2):
  print('no')
elif(myinputs % 1 ==0 and myinputs % temp==0 and myinputs%2!=0 and myinputs%3!=0 and myinputs%4!=0):
  print('no')
else:
  print('yes')
