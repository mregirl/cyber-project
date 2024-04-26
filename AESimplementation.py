import AES
import time
from Crypto.Util.Padding import unpad

# --------------AES in ECB mode--------------
print("--AES in ECB mode--")
AES_ECB=AES.AESinECB()

# Open test file
with open('/home/anon/Uni/CyberSec/Project/test_files/500MB.txt', 'r') as file:
            msg = file.read()

# Print input message (will not be used for testing large files) and key
#print("Plaintext: '"+msg+"'")
print("Key: '"+AES_ECB.getKey().hex()+"'")

# Start encryption           
start_time1 = time.time()
ciphertxt=AES_ECB.encrypt(msg)
encryption_time=time.time() - start_time1

# Print encryption results (will not be used for testing large files)
#print("Ciphertext: '"+ciphertxt.hex()+"'")

# Start decryption
start_time2 = time.time()
plaintxt=unpad(AES_ECB.decrypt(ciphertxt),16)
decryption_time=time.time() - start_time2

# Print decryption results (will not be used for testing large files)
#print("Decrypted Plaintext: '"+plaintxt.decode('latin-1')+"'")

# Print encryption and decryption time
print("Encryption time: %s sec" %encryption_time)
print("Decryption time: %s sec" %decryption_time)
