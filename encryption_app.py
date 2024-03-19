from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import argparse
import logging


def derive_key(key):
    # Derive a 32-byte (256-bit) key using PBKDF2
    salt = b"salt1234"  # You should use a unique salt for each application
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,  # Adjust the number of iterations as needed for your security requirements
        backend=default_backend(),
    )
    return kdf.derive(key)


def encrypt(plaintext, key):
    key = derive_key(key.encode("utf-8"))
    cipher = Cipher(
        algorithms.AES(key), modes.CFB8(key[:16]), backend=default_backend()
    )
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return base64.b64encode(ciphertext).decode("utf-8")


def decrypt(ciphertext, key):
    key = derive_key(key.encode("utf-8"))
    cipher = Cipher(
        algorithms.AES(key), modes.CFB8(key[:16]), backend=default_backend()
    )
    decryptor = cipher.decryptor()
    ciphertext_bytes = base64.b64decode(ciphertext)
    plaintext = decryptor.update(ciphertext_bytes) + decryptor.finalize()
    return plaintext.decode("utf-8")


def main():
    parser = argparse.ArgumentParser(description="Simple AES Encryption and Decryption")
    parser.add_argument(
        "mode",
        choices=["encrypt", "decrypt"],
        help='Select "encrypt" or "decrypt" mode',
    )
    parser.add_argument("-p", "--plaintext", help="Text to be encrypted or decrypted")
    parser.add_argument("-k", "--key", help="Encryption/Decryption key")

    args = parser.parse_args()

    if args.mode == "encrypt":
        if not args.plaintext or not args.key:
            print("Error: Both plaintext and key are required for encryption.")
            return
        encrypted_text = encrypt(args.plaintext.encode("utf-8"), args.key)
        print(f"Encrypted Text: {encrypted_text}")

    elif args.mode == "decrypt":
        if not args.plaintext or not args.key:
            print("Error: Both ciphertext and key are required for decryption.")
            return
        decrypted_text = decrypt(args.plaintext, args.key)
        print(f"Decrypted Text: {decrypted_text}")


if __name__ == "__main__":
    main()
