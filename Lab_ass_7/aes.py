from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import ecc
def gen_key():
    return ecc.gen_key_from_ecc()
def encrypt_text(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    message_bytes = message.encode('utf-8')
    ciphertext, tag = cipher.encrypt_and_digest(message_bytes)
    return cipher.nonce, ciphertext, tag
def decrypt_text(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_data.decode('utf-8')
    except ValueError:
        print("Decryption failed! Invalid key or corrupted data.")
        return None
if __name__ == "__main__":
    message = input("Enter the message to encrypt: ")
    key = gen_key()
    nonce, encrypted_data, tag = encrypt_text(message, key)
    print(f"Encrypted data: {encrypted_data}")
    decrypted_data = decrypt_text(nonce, encrypted_data, tag, key)
    if decrypted_data:
        print(f"Decrypted message: {decrypted_data}")
    else:
        print("Decryption failed.")
