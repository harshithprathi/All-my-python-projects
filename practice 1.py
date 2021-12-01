a=int(input())
list1=[]
for i in range(0,a):
    b=input()
    list1.append(b)
for i in range(0,len(list1)):
    x=list1[i]
    y=list1[i+1]
    if(x[0]==y[0]):
        del list1[i]
for i in range(0,len(list1)):
    print(list1[i])
    
