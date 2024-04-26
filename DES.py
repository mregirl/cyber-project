from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from secrets import token_bytes

# DES in ECB mode
class DESinECB():
    def __init__(self):
        # Generate a pseudo-random key with a size of 8 bytes
        self.key=token_bytes(8)
        self.des=DES.new(self.key,DES.MODE_ECB)
    def encrypt(self,msg):
        padded_msg=pad(msg.encode("utf-8"),8) # need to do padding since ECB will take full byte
        ciphertxt=self.des.encrypt(padded_msg)
        return ciphertxt
    def decrypt(self, cipher):
        return self.des.decrypt(cipher)
    def getKey(self):
        return self.key
