import os 
import pyaes
## open the encrypted
file_name = 'test.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()
## key for decryption
key = b"testransomwaretroll"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)
## remove encrypted file
os.remove(file_name)
## create the decrypted file 
new_file = "test.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
