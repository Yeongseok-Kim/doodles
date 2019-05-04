x=int(input("십진수를 입력하시오: "))
i=''

while x>0:
    i=str(x%2)+i
    x=x//2

print(i)