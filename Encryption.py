import hashlib
import bcrypt

password = input("Enter your password : \n")
byte_password = bytes(password,'utf-8')

print("********************************************    (sha1)     ************************************************")
for i in range(3):
    hash_password = hashlib.sha1(byte_password)
    pw = hash_password.hexdigest()
    print(pw)


print("\n*******************************************      (MD5)       **********************************************")
for i in range(3):
    hash_password = hashlib.md5(byte_password)
    pw1 = hash_password.hexdigest()
    print(pw1)

print("\n*******************************************     (bcrypt)   ************************************************")
for i in range(3):
    pw2 = bcrypt.hashpw(byte_password,bcrypt.gensalt(10))
    print(pw2)

