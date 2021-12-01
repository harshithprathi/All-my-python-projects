N=int(input())
list1=[]
for i in range(1,100):
    x=i*i 
    list1.append(x)
if(N<0):
    print("Error")
elif(N==0):
    print("0")
else:
    print(list1[N-1])
