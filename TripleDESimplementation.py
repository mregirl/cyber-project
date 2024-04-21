import TripleDES
import time
from Crypto.Util.Padding import unpad

# --------------3DES in ECB mode--------------
print("--3DES in ECB mode--")
TripleDES_ECB=TripleDES.TripleDESinECB()

# Open test file
with open('test_files/100MB.txt', 'r') as file:
            msg = file.read()

# Print input message (will not be used for testing large files) and key
#print("Plaintext: '"+msg+"'")
print("Key: '"+TripleDES.key.hex()+"'")

# Start encryption           
start_time1 = time.time()
ciphertxt=TripleDES_ECB.encrypt(msg)
encryption_time=time.time() - start_time1

# Print encryption results (will not be used for testing large files)
#print("Ciphertext: '"+ciphertxt.hex()+"'")

# Start decryption
start_time2 = time.time()
plaintxt=unpad(TripleDES_ECB.decrypt(ciphertxt),8)
decryption_time=time.time() - start_time2

# Print decryption results (will not be used for testing large files)
#print("Decrypted Plaintext: '"+plaintxt.decode('latin-1')+"'")

# Print encryption and decryption time
print("Encryption time: %s sec" %encryption_time)
print("Decryption time: %s sec" %decryption_time)