import socket
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def receiver(n, g):
    y = random.randint(2, 10)
    k2 = pow(g, y, n)
    return k2, y

def shared_key_receiver(k1, y, n):
    return pow(k1, y, n)

def compute_hash(message):
    return hashlib.sha512(message.encode()).digest()
 
def aes_decrypt(encrypted_message, key):
    iv = encrypted_message[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_message[16:]), AES.block_size)
    
    message = decrypted[:-32].decode()
    received_hash = decrypted[-32:]

    expected_hash = compute_hash(message)

    if received_hash == expected_hash:
        print("\nIntegrity Check Passed ")
        return message
    else:
        print("\nIntegrity Check Failed ")
        return None

def server():
    n = int(input("Enter the value of n: "))
    g = int(input("Enter the primitive root g: "))

    k2, y = receiver(n, g)
    print("Receiver's public key:", k2)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is waiting for a connection...")

    client_socket, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    client_socket.send(str(k2).encode())
    public_sender = int(client_socket.recv(1024).decode())

    shared_key = shared_key_receiver(public_sender, y, n)
    print(f"Shared secret key: {shared_key}")

    aes_key = hashlib.sha512(str(shared_key).encode()).digest()[:16]

    encrypted_message = client_socket.recv(1024)
    decrypted_message = aes_decrypt(encrypted_message, aes_key)

    if decrypted_message:
        print(f"Decrypted Message: {decrypted_message}")

    client_socket.close()
    server_socket.close()

server()
