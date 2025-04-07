import socket
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib

def sender(n, g):
    x = random.randint(2, 10)
    k1 = pow(g, x, n)
    return k1, x

def shared_key_sender(k2, x, n):
    return pow(k2, x, n)

def compute_hash(message):
    return hashlib.sha512(message.encode()).digest()

def aes_encrypt(message, key):
    hash_code = compute_hash(message)
    combined_data = message.encode() + hash_code
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted = cipher.encrypt(pad(combined_data, AES.block_size))
    return cipher.iv + encrypted

def client():
    n = int(input("Enter the value of n: "))
    g = int(input("Enter the primitive root g: "))
    
    k1, x = sender(n, g)
    print("Sender's public key:", k1)
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    public_receiver = int(client_socket.recv(1024).decode())
    client_socket.send(str(k1).encode())

    shared_key = shared_key_sender(public_receiver, x, n)
    print(f"Shared secret key: {shared_key}")

    aes_key = hashlib.sha512(str(shared_key).encode()).digest()[:16]

    message = input("Enter the message to send: ")
    encrypted_message = aes_encrypt(message, aes_key)
    
    print(f"Encrypted message: {encrypted_message.hex()}")
    
    client_socket.send(encrypted_message)
    client_socket.close()

client()
