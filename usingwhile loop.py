n=int(input("enter the no."))
s=0;
a=2
while(a<=n):
    if(s%2==0):
        s=s+a
        a=a+2
print("sum of series=",s)
s=0
a=1
while(a<=n):
    if(s%2!=2):
        s=s+a
        a=a+1
print("sum of odd series=",s)        
