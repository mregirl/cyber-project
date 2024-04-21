from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secrets import token_bytes

# Generate a pseudo-random key with a size of 16 bytes
key=token_bytes(16)

class AESinECB():
    def __init__(self):
        self.aes=AES.new(key,AES.MODE_ECB)
    def encrypt(self,msg):
        padded_msg=pad(msg.encode("utf-8"),16) # need to do padding since AES block size is 16 bytes
        ciphertxt=self.aes.encrypt(padded_msg)
        return ciphertxt
    def decrypt(self, cipher):
        return self.aes.decrypt(cipher)