n=int(input('enter a num ='))
t=1
if (n<1):
    t=1
for b in range(2,n):
    if n%b==0:
        t=0
        break

if t==0:
    print('not prime number')
else:
    print('prime number')
    
        
