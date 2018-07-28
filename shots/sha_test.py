import hashlib

sha1 = hashlib.sha1()
sha1.update("czk10101".encode('utf-8'))
print(sha1.hexdigest())
sha1.update("czk10102".encode('utf-8'))
print(sha1.hexdigest())
sha1.update("czk10101".encode('utf-8'))

print(sha1.hexdigest())
md5 = hashlib.md5()
md5.update('czk10101'.encode('utf-8'))
print(md5.hexdigest())
