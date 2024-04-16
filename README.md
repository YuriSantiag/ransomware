# Simple Ransomware in Python

This is a basic example of a ransomware implemented in Python, designed for educational and demonstration purposes. The code is capable of encrypting and decrypting files using the AES (Advanced Encryption Standard) algorithm through the pyaes library.

## How It Works

The ransomware consists of two separate Python scripts:

encrypt.py: This script encrypts an input file and renames it with a specific extension (".ransomwaretroll" in this example).
decrypt.py: This script decrypts a file encrypted by the encrypt.py script and restores its original name and content.
## Requirements

Make sure you have Python installed on your system. You will also need to install the pyaes library. You can install it via pip:

```
pip install pyaes

```
## Usage

Place the files you want to encrypt or decrypt in the same directory as the Python scripts.
Run encrypt.py to encrypt a file:
```
python encrypt.py
```
Run decrypt.py to decrypt the encrypted file:
```
python decrypt.py
```
