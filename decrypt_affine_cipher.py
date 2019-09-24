ciphertext='FALSZZTYSYJZYJKYWJRZTYJZTYYNARYJKYSWARZTYEGYYJ'

for i in ciphertext:
    plaintext=ord(i)-65
    plaintext-=22
    plaintext*=15
    plaintext%=26
    plaintext=chr(plaintext+65)
    print(plaintext,end='')
