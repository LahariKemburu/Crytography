import socket
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
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))
key = client.recv(16)
file_name = input("Enter file name: ")
client.sendall(file_name.encode())
data = client.recv(1000000)
if data == b"ERROR":
    print("File not found.")
else:
    with open("encrypted_data.txt", "wb") as enc_file:
        enc_file.write(data)
    print("Encrypted data saved as 'encrypted_data'.")
    decrypted_data = rc4(data, key)
    with open("decrypted.txt", "wb") as dec_file:
        dec_file.write(decrypted_data)
    print("Decrypted file saved as 'decrypted.txt'.")

client.close()
