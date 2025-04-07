import random
p = 23
g = 5
prv_a = random.randint(1, p-1)
prv_b = random.randint(1, p-1)
pub_a = pow(g, prv_a, p)
pub_b = pow(g, prv_b, p)
secret_key_a = pow(pub_b, prv_a, p)
secret_key_b = pow(pub_a, prv_b, p)
print(f"Private Key of A: {prv_a}")
print(f"Private Key of B: {prv_b}")
print(f"Public Key of A: {pub_a}")
print(f"Public Key of B: {pub_b}")
print(f"Shared Secret (A): {secret_key_a}")
print(f"Shared Secret (B): {secret_key_b}")
assert secret_key_a == secret_key_b, "Key exchange failed!"
