from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secrets import token_bytes

class AESinECB():
    def __init__(self):
        # Generate a pseudo-random key with a size of 16 bytes
        self.key=token_bytes(16)
        self.aes=AES.new(self.key,AES.MODE_ECB)
    def encrypt(self,msg):
        padded_msg=pad(msg.encode("utf-8"),16) # need to do padding since AES block size is 16 bytes
        ciphertxt=self.aes.encrypt(padded_msg)
        return ciphertxt
    def decrypt(self, cipher):
        return self.aes.decrypt(cipher)
    def getKey(self):
        return self.key
