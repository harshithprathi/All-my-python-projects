simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
x=simple_string.split()
a=[]
for i in x:
    y=i[0]
    if(y.isupper()==True):
        a.append(i)
print(a)

