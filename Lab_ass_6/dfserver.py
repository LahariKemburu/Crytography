import socket
import random
p = 23
g = 5
server_private = random.randint(1, p-1)
server_public = pow(g, server_private, p)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12345))
server.listen(1)
conn, addr = server.accept()
client_public = int(conn.recv(1024).decode())
conn.send(str(server_public).encode())
shared_key = pow(client_public, server_private, p)
shift = shared_key % 26
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
message = "Hello Client"
encrypted_message = caesar_cipher(message, shift)
conn.send(encrypted_message.encode())
conn.close()
server.close()
