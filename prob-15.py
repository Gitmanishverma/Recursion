# Product of two elements using recurion without using * 

def product(x,y):
  if x<y:
    return product(y,x)
  elif y!=0:
    return x+product(x,y-1) 
  else:
    return 0
  

print(product(3,4))