from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("New key generated and saved as 'secret.key'.")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    with open("vault.bin", "wb") as vault_file:
        vault_file.write(encrypted_message)
    print("Message locked in vault.bin")

def decrypt_message():
    key = load_key()
    f = Fernet(key)
    with open("vault.bin", "rb") as vault_file:
        encrypted_message = vault_file.read()
    decrypted_message = f.decrypt(encrypted_message)
    print(f"Decrypted Content: {decrypted_message.decode()}")

# Simple Menu
print("1. Gen Key | 2. Encrypt | 3. Decrypt")
choice = input("Choice: ")
if choice == '1': generate_key()
elif choice == '2': encrypt_message(input("Enter secret: "))
elif choice == '3': decrypt_message()
