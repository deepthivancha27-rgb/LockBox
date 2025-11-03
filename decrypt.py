from cryptography.fernet import Fernet

# Read the key from the file
with open('encrypt.key', 'rb') as key_file:
    key = key_file.read()

# Read the encrypted file
with open('secret.enc', 'rb') as file:
    encrypted_data = file.read()

# Decrypt the data
cipher = Fernet(key)
decrypted_data = cipher.decrypt(encrypted_data)

# Save the decrypted data to a new file
with open('secret.dec', 'wb') as file:
    file.write(decrypted_data)