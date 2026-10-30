import rsa
private_key = rsa.Privatekey.load_pkcs1(open("private_key.txt",'rb').read())
encrypted = open('encrypted.bin','rb').read()
decrypted = rsa.decrypt(encrypted, private_keys)

print('Decrypted',decrypted.decode())