import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import hashlib #takes in input data and produces a statistically unique output
import base64  #is used to convert bytes that have binary or text data into ASCII characters
KEY = b'1234567890abcdef'  # 16-byte key
IV = b'1234567890abcdef'  # Iitialization vector used for randomness
# Function to encrypt data
def encrypt_data(data):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(encrypted).decode()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Set up the client
client.connect(('localhost', 12345))
message = "Hello, Server! This is a secure message."# Message to send
encrypted_message = encrypt_data(message)# Encrypt the message
print("Encrypted message:", encrypted_message)# Send the encrypted data
client.send(encrypted_message.encode())
encrypted_response = client.recv(1024).decode()# Receive the encrypted response
print("Encrypted response:", encrypted_response)
client.close()
