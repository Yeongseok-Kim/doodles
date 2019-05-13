while True:
    import random
    x=random.randrange(100,1000)
    xl=[x//100,(x//10)-((x//100)*10),x-((x//10)*10)]
    if xl[0]!=xl[1]!=xl[2] and xl[0]!=xl[2]:
        break

chance=1

while True:
    b=0
    s=0
    o=0
    while True:
        y=int(input("%d회, 값을 입력하시오: "%chance))
        yl=[y//100,(y//10)-((y//100)*10),y-((y//10)*10)]
        if yl[0]!=yl[1]!=yl[2] and yl[0]!=yl[2]:
            break
        else:
            print("잘못된 입력입니다!")
    for i in range(0,3):
        if yl[i]==xl[i]:
            s=s+1
        elif xl.count(yl[i])==1:
            b=b+1
    if s==3:
        print("승리하였습니다!")
        break
    elif s==0 and b==0:
        o=1
    print("B:%d S:%d O:%d"%(b,s,o))
    if chance==9:
        print("패배하였습니다!")
        break
    else:
        chance=chance+1