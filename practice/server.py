import socket

s = socket.socket()
s.bind(("127.0.0.1", 12345))
s.listen()

c, addr = s.accept()
print("Connected:", addr)

while True:
    msg = c.recv(1024).decode()
    if msg.lower() == "bye":
        print("Client left. Closing connection.")
        break
    print("Client:", msg)
    
    reply = input("Server: ")
    c.send(reply.encode())

c.close()
s.close()
