list=[0,0,0,0,0,0,0,0,0,0]
str=input()
for i in str:
    if i.isdigit():
        list[int(i)]=str.count(i)
for j in list:
    print(j,end=" ")