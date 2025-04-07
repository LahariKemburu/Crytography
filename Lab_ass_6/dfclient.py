import socket
import random
p = 23
g = 5
client_private = random.randint(1, p-1)
client_public = pow(g, client_private, p)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345))
client.send(str(client_public).encode())
server_public = int(client.recv(1024).decode())
shared_key = pow(server_public, client_private, p)
shift = shared_key % 26
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result
encrypted_message = client.recv(1024).decode()
decrypted_message = caesar_cipher(encrypted_message, shift)
print(f"Decrypted Message: {decrypted_message}")
client.close()
