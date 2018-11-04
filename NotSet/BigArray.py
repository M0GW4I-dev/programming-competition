N,K=[int(i) for i in input().split()]
data=list()
for i in range(0,N):
    data.append([int(i) for i in input().split()])
newdata=sorted(data,key=lambda d:d[0])
count=0
for d in newdata:
    count+=d[1]
    if count>=K:
        print(d[0])
        break





    
