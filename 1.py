import requests
from simplecrypt import decrypt, DecryptionException


'''with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt", "r") as passw:
    pstr = passw.read().split()
    print(encrypted)
    s = decrypt(pstr[3], encrypted)
    print(s)'''

for k in pstr:
    print(k)
    try:
        s = decrypt(k, encrypted)
        print(s)
    except DecryptionException:
        pass
    else:
        print(k, s)




