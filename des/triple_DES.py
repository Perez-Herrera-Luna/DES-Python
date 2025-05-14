# Luna Perez-Herrera
# GNU AGPLv3

"""Module providing a Triple DES implementation"""

from des import DES


class TripleDES:
    """Class for a Triple DES object. Capable of encrypting or decrypting an input with a key"""

    def __init__(self, key: str):
        key1, key2, key3 = self.__split_key(key)
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

    def __split_key(self, key) -> str:
        self.__validate_key(key)

        if len(key) == 34:
            key1 = "0x" + key[2:18]
            key2 = "0x" + key[18:34]
            key3 = None
        else:
            key1 = "0x" + key[2:18]
            key2 = "0x" + key[18:34]
            key3 = "0x" + key[34:50]

        return key1, key2, key3

    # Validates key, cleartext, and ciphertext input
    def __validate_key(self, key: str):
        if not "0x" in key[:2]:
            raise ValueError('Key has no leading "0x"')

        if len(key) != 34 and len(key) != 50:
            raise ValueError("Key is of invalid length")

        valid_set = {
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
        }

        for char in key[2:].upper():
            if char not in valid_set:
                raise ValueError("Invalid hex string. Characters in key should be 0-f")
