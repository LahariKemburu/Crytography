import sympy
import random
import socket

def cal_e(phi):
    e = random.randint(2, phi - 1)
    while sympy.gcd(phi, e) != 1:
        e = random.randint(2, phi - 1)
    return e

a = int(input("Enter the starting range of prime numbers: "))
b = int(input("Enter the ending range of prime numbers: "))
primes = list(sympy.primerange(a, b))

p = random.choice(primes)
q = random.choice([x for x in primes if x != p])

print("p is", p, "q is", q)

n = p * q
phi = (p - 1) * (q - 1)

e = cal_e(phi)
d = pow(e, -1, phi)

print("Public key is (", e, ",", n, ")")
print("Private key is (", d, ",", n, ")")

data = input("Enter the plain text: ")
data_nums = [ord(ch) for ch in data]
encrypted_data = [pow(num, e, n) for num in data_nums]
print(f"Encrypted data: {encrypted_data}")

decrypted_data = [chr(pow(num, d, n)) for num in encrypted_data]
decrypted_text = ''.join(decrypted_data)

if all(32 <= ord(ch) <= 126 for ch in decrypted_text):
    print(f"Decrypted data: {decrypted_text}")
else:
    print("Decryption failed. Non-printable characters detected.")
