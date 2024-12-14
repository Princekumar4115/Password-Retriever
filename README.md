Explanation of the Code
Key Generation: The generate_key() function creates a new encryption key using the Fernet symmetric encryption method.
Key Management: The key is saved to a file (secret.key) for later use. The load_key() function reads the key from this file.
Password Encryption/Decryption: The encrypt_password() and decrypt_password() functions handle the encryption and decryption of passwords.
Data Storage: Passwords are stored in a JSON file (passwords.json). The save_passwords() and load_passwords() functions manage this file.
User Interface: The main loop allows users to add passwords, retrieve passwords, or exit the program.
