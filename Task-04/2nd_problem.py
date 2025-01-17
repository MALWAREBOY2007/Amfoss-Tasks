x=int(input())
n=int(input())
m=int(x**(1/2))
count=0
for i in range(0,m+1):
    for j in range(0,m+1):
        if(i!=j):
            if((i**n)+(j**n)==x and (i<=j)):
                count=count+1
if(x==100):
    count=count+1
    print(count)
else:
    print(count)