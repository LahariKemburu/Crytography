import sympy
import random
import socket

def cal_e(phi):
    e = random.randint(2, phi - 1)
    while sympy.gcd(phi, e) != 1:
        e = random.randint(2, phi - 1)
    return e

def generate_keys():
    primes = list(sympy.primerange(100, 500))
    p, q = random.sample(primes, 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = cal_e(phi)
    d = pow(e, -1, phi)
    return (e, n), (d, n)

server_public, server_private = generate_keys()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))
server.listen(1)

conn, addr = server.accept()

conn.send(f"{server_public[0]},{server_public[1]}".encode())
client_public = tuple(map(int, conn.recv(1024).decode().split(',')))

while True:
    encrypted_data = conn.recv(4096).decode()
    if not encrypted_data:
        break

    encrypted_list = list(map(int, encrypted_data.split(',')))
    decrypted_data = ''.join([chr(pow(num, server_private[0], server_private[1])) for num in encrypted_list])
    print(f"Client: {decrypted_data}")

    reply = input("Server: ")
    encrypted_reply = [pow(ord(ch), client_public[0], client_public[1]) for ch in reply]
    conn.send(",".join(map(str, encrypted_reply)).encode())

conn.close()  
server.close()
