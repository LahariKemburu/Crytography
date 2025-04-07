import socket

s = socket.socket()
s.connect(("127.0.0.1", 12345))

while True:
    msg = input("Client: ")
    s.send(msg.encode())
    
    if msg.lower() == "bye":
        print("Closing connection.")
        break

    reply = s.recv(1024).decode()
    print("Server:", reply)

s.close()
