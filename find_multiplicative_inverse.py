def find_inverse(a,b):
    q=1
    while True:
        if (a*q)%b==1:
            return q
        q+=1

print(find_inverse(7,31))
print(find_inverse(18,31))
print(find_inverse(25,31))