import socket
from Crypto.Random import get_random_bytes
def rc4(data, key):
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    i = j = 0
    key_stream = bytearray()
    for byte in data:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        key_stream.append(byte ^ s[(s[i] + s[j]) % 256])
    return bytes(key_stream)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))
server.listen(1)
print("Server listening...")
conn, addr = server.accept()
key = get_random_bytes(16)
conn.sendall(key)
file_name = conn.recv(1024).decode()
try:
    with open(file_name, "rb") as f:
        data = f.read()
    encrypted_data = rc4(data, key)
    conn.sendall(encrypted_data)
except FileNotFoundError:
    conn.sendall(b"ERROR")
conn.close()
server.close()
