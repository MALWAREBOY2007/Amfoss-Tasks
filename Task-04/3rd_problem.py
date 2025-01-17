n=int(input())
listA=list(map(int,input().split()))
for i in listA:
        if(listA.count(i)==1):
            print(i)
            break