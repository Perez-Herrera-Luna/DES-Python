# Luna Perez-Herrera
# GNU AGPLv3

"""Module providing a Triple DES implementation"""

from des import DES


class TripleDES:
    """Class for a Triple DES object. Capable of encrypting or decrypting an input with a key"""

    def __init__(self, key1: str, key2: str, key3: str = None):
        self.key1 = key1
        self.key2 = key2
        self.key3 = key3 if key3 else key1

        self.__des1 = DES.DES(self.key1)
        self.__des2 = DES.DES(self.key2)
        self.__des3 = DES.DES(self.key3)

    def encrypt(self, plaintext: str) -> str:
        """Encrypts the input plaintext by the key"""
        plaintext = self.__des1.encrypt(plaintext)
        plaintext = self.__des2.decrypt(plaintext)
        plaintext = self.__des3.encrypt(plaintext)

        return plaintext

    def decrypt(self, ciphertext: str) -> str:
        """Decrypts the input ciphertext by the key"""
        ciphertext = self.__des3.decrypt(ciphertext)
        ciphertext = self.__des2.encrypt(ciphertext)
        ciphertext = self.__des1.decrypt(ciphertext)

        return ciphertext
