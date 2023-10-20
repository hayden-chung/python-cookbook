def recursion (n, product):
    if n != 1:
        product *= n
        recursion (n-1, product)
    else: 
        print(product)

def whileLoop (n, product):
    while n != 0:
        product *= n 
        n -= 1 
    return product
    

# if n == 3:
# 3*2 


# recursion(6, 1)
# print(whileLoop(6, 1))

def recursionAnswer(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * recursionAnswer(n-1)
    
print(recursionAnswer(6))

