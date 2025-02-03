import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
import base64
# Define AES key and initialization vector (must be 16 bytes for AES-128)
KEY = b'1234567890abcdef'  # Example 16-byte key
IV = b'1234567890abcdef'  # Example 16-byte IV
def decrypt_data(encrypted_data):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    decrypted = unpad(cipher.decrypt(base64.b64decode(encrypted_data)), AES.block_size)
    return decrypted.decode()
#server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print("Server is listening...")
while True:
    client_socket, client_address = server.accept()
    print(f"Connection from {client_address}")
    encrypted_data = client_socket.recv(1024).decode()
    print("Encrypted message received:", encrypted_data)
    decrypted_message = decrypt_data(encrypted_data)
    print("Decrypted message:", decrypted_message)
    encrypted_response = base64.b64encode(AES.new(KEY, AES.MODE_CBC, IV).encrypt(AES.block_size * b'\0')).decode()
    client_socket.send(encrypted_response.encode())
    client_socket.close()
