number=input('16진수 한 글자 입력: ')
number=ord(number)

if 47<number<58 or 64<number<71 or 96<number<103:
    number=chr(number)
    print('10진수 ==> %d'%int(number,16))
else:
    print('16진수가 아닙니다')