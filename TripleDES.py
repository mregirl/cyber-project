from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from secrets import token_bytes

# Generate 3 pseudo-random keys with a size of 16 bytes
while True:
    try:
        key = DES3.adjust_key_parity(token_bytes(24))
        break
    except ValueError:
        pass
class TripleDESinECB():
    def __init__(self):
        self.des3=DES3.new(key,DES3.MODE_ECB)
    def encrypt(self,msg):
        padded_msg=pad(msg.encode("utf-8"),8) # need to do padding since 3DES block size is 8 bytes
        ciphertxt=self.des3.encrypt(padded_msg)
        return ciphertxt
    def decrypt(self, cipher):
        return self.des3.decrypt(cipher)
