def fact(n):
    if n==1:
        return 1
    '''
    if n==0:
        return 0'''
    return n*fact(n-1)
x=fact(5)
print(x)