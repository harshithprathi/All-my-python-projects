def even(x):
    for n in range(0,x):
        if x%2==0:
            return True
        else:
            return False
filtered=filter(even,range(10))
print(list(filtered))
