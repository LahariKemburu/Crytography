import hashlib
msg=input("Enter the message: ")
res=hashlib.sha512(msg.encode())
print(res.hexdigest())
