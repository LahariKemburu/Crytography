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

client_public, client_private = generate_keys()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))

server_public = tuple(map(int, client.recv(1024).decode().split(',')))
client.send(f"{client_public[0]},{client_public[1]}".encode())

while True:
    message = input("Client: ")
    encrypted_data = [pow(ord(ch), server_public[0], server_public[1]) for ch in message]
    client.send(",".join(map(str, encrypted_data)).encode())

    encrypted_reply = client.recv(4096).decode()
    if not encrypted_reply:
        break

    decrypted_reply = ''.join([chr(pow(int(num), client_private[0], client_private[1])) for num in encrypted_reply.split(',')])
    print(f"Server: {decrypted_reply}")

client.close()
