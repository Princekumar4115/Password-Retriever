import json
import os
from cryptography.fernet import Fernet


# Function to generate a key for encryption
def generate_key():
    return Fernet.generate_key()


# Function to load the key from a file
def load_key():
    return open("secret.key", "rb").read()


# Function to save the key to a file
def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


# Function to encrypt a password
def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password


# Function to decrypt a password
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password


# Function to save passwords to a JSON file
def save_passwords(passwords):
    with open("passwords.json", "w") as f:
        json.dump(passwords, f)


# Function to load passwords from a JSON file
def load_passwords():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as f:
            return json.load(f)
    return {}


# Main function to run the password manager
def main():
    # Check if the key file exists, if not, generate a new key
    if not os.path.exists("secret.key"):
        key = generate_key()
        save_key(key)
    else:
        key = load_key()

    passwords = load_passwords()

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            site = input("Enter the site name: ")
            password = input("Enter the password: ")
            encrypted_password = encrypt_password(password, key)
            passwords[site] = encrypted_password.decode()  # Store as string
            save_passwords(passwords)
            print("Password added successfully.")

        elif choice == '2':
            site = input("Enter the site name: ")
            if site in passwords:
                encrypted_password = passwords[
                    site].encode()  # Convert back to bytes
                decrypted_password = decrypt_password(encrypted_password, key)
                print(f"Password for {site}: {decrypted_password}")
            else:
                print("No password found for that site.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
