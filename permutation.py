def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def permutation(n,s):
    for i in range(1,n+1):
        s[i-1]=i
    print(s)
    for i in range(2,factorial(n)+1):
        m=n-1
        while s[m-1]>s[m]:
            m=m-1
        k=n
        while s[m-1]>s[k-1]:
            k=k-1
        swap=s[m-1]
        s[m-1]=s[k-1]
        s[k-1]=swap
        p=m+1
        q=n
        while p<q:
            swap=s[p-1]
            s[p-1]=s[q-1]
            s[q-1]=swap
            p=p+1
            q=q-1
        print(s)

s=[1,2,3,4,5,6]
n=4
permutation(s,n)