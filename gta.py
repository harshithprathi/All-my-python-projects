import ast
input_str = input()
input_list = ast.literal_eval(input_str)
m = int(input_list[0])  
c = int(input_list[1])  
n = int(input_list[2])  
k = int(input_list[3])  
choc = m//c        
w = m//c               
while (w//n!=0):
  wrap = (w//n)*k
  choc = choc + wrap
  w = wrap + w%n
print(choc)
