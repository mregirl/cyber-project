from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from secrets import token_bytes

# Generate a pseudo-random key with a size of 8 bytes
key=token_bytes(8)

# DES in ECB mode
class DESinECB():
    def __init__(self):
        self.des=DES.new(key,DES.MODE_ECB)
    def encrypt(self,msg):
        padded_msg=pad(msg.encode("utf-8"),8) # need to do padding since ECB will take full byte
        ciphertxt=self.des.encrypt(padded_msg)
        return ciphertxt
    def decrypt(self, cipher):
        return self.des.decrypt(cipher)
