# LockBox: Secure File Encryption System

## Overview
This project demonstrates how to encrypt and decrypt sensitive files using Python and the Fernet library (AES encryption).

## How It Works
- *Encryption*: Files are encrypted using a secret key. Only those with the key can decrypt.
- *Decryption*: The encrypted file is decrypted using the same key.

## Security Best Practices
- *Key Management*: Never expose your encryption key. Store it securely and rotate it regularly.
- *Data at Rest*: Encrypted files are safe even if someone gains access to your storage.
- *Data in Motion*: Encrypted files can be safely transmitted over networks.

## Usage
1. Install dependencies: pip install cryptography
2. Run encrypt.py to encrypt a file.
3. Run decrypt.py to decrypt a file.

## Important
- Do not commit your key file (encrypt.key) to GitHub.
- Use secure key storage for production environments.