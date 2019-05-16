import math

def is_prime(n):
    for d in range(2,int((math.sqrt(n)//1))+1):
        if(n%d==0):
            return d
    return 0

n=int(input())
print(is_prime(n))