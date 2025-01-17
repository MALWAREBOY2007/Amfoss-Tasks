n=int(input())
listA=list(map(int,input().split()))
m=int(input())
listB=list(map(int,input().split()))
for i in listB:
    for j in listA:
        if(i==j):
            listB.remove(i)
            listA.remove(i)
listB.sort()
listB=set(listB)
for i in listB:
    print(i,end=" ")