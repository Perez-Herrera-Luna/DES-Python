# Luna Perez-Herrera
# GNU AGPLv3

"""Module providing a DES implementation for encryption"""

import constants


class DES:
    """Class for a DES object. Capable of encrypting or decrypting an input with a key"""

    def __init__(self, key: str):
        # Key should be a 64 bit hexadexcimal string with no leading '0x'
        self.key = bin(int(key, 16))[2:].zfill(64)

        self.__pc1 = constants.des_pc1()
        self.__pc2 = constants.des_pc2()
        self.__shifts = constants.des_shifts()
        self.__ip = constants.des_ip()
        self.__fp = constants.des_fp()
        self.__ep = constants.des_ep()
        self.__pf = constants.des_pf()
        self.__sboxes = constants.des_sboxes()
        self.__round_keys = self.__generate_round_keys()
        self.__round_keys_reversed = self.__round_keys[::-1]

    def encrypt(self, plaintext: str) -> str:
        """Encrypts the input plaintext by the key"""
        # Plaintext should be a 64 bit hexadecimal string with no leading '0x'
        plaintext = bin(int(plaintext, 16))[2:].zfill(64)

        # Preform initial permutation
        plaintext = self.__permute(plaintext, self.__ip)

        # Split into two halves
        l = [plaintext[:32]]
        r = [plaintext[32:]]

        # Perform 16 rounds of DES
        for i in range(16):
            l.append(r[i])
            r.append(self.__xor(l[i], self.__f(r[i], self.__round_keys[i])))

        # Preform final permutation
        ciphertext = self.__permute(r[16] + l[16], self.__fp)

        return self.__format_as_hex(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        """Decryptes the input ciphertext by the key"""
        # Ciphertext should be a 64 bit hexadecimal string with no leading '0x'
        ciphertext = bin(int(ciphertext, 16))[2:].zfill(64)

        # Perform intial permutation
        ciphertext = self.__permute(ciphertext, self.__ip)

        # Split into two halves
        l = [ciphertext[:32]]
        r = [ciphertext[32:]]

        # Perform 16 rounds of DES
        for i in range(16):
            l.append(r[i])
            r.append(self.__xor(l[i], self.__f(r[i], self.__round_keys_reversed[i])))

        # Preform final permutation
        cleartext = self.__permute(r[16] + l[16], self.__fp)

        return self.__format_as_hex(cleartext)

    # Generates the 16 rounds keys used in DES
    def __generate_round_keys(self):
        # Apply PC-1
        temp_key = self.__permute(self.key, self.__pc1)

        # Split into two halves
        c_keys = [temp_key[:28]]
        d_keys = [temp_key[28:]]

        # Generate 16 'c' and 'd' keys
        for i in range(16):
            c_keys.append(self.__shift_left(c_keys[i], self.__shifts[i]))
            d_keys.append(self.__shift_left(d_keys[i], self.__shifts[i]))

        # List to store round keys
        round_keys = []

        # Append 'c' and 'd' keys to form round keys
        for i in range(1, 17):
            key_i = c_keys[i] + d_keys[i]
            round_keys.append(self.__permute(key_i, self.__pc2))  # Permute with PC-2

        return round_keys

    # Permutes the input according to the table. Used for all the fancy permutations in DES
    def __permute(self, key, table):
        permuted_key = ""

        # Permute the key according to the table
        for i in table:
            permuted_key += key[i - 1]
            # The -1 is because all the tables are 1-indexed, but arrays are 0-indexed

        return permuted_key

    # Preforms the S-box substitution in the DES algorithm
    def __s_box_substitution(self, R):
        # Split into 8 blocks of 6 bits
        blocks = [R[i : i + 6] for i in range(0, len(R), 6)]

        # Perform S-box substitution
        for i, block in enumerate(blocks):
            row = int(block[0] + block[5], 2)  # First and last bit
            col = int(block[1:5], 2)  # Middle 4 bits
            blocks[i] = format(self.__sboxes[i][row][col], "04b")  # Format to 4 bits

        # Concatenates the blocks. Think of this as flattening the list
        return "".join(blocks)

    # Preforms the XOR operation on two binary strings
    def __xor(self, a, b):
        # XORs each bit one by one
        return "".join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    # Preforms the f function in the DES algorithm
    def __f(self, r, k):
        # Perform expansion permutation
        r = self.__permute(r, self.__ep)

        # XOR with input
        r = self.__xor(r, k)

        # Perform S-box substitution
        r = self.__s_box_substitution(r)

        # Perform permutation
        r = self.__permute(r, self.__pf)

        return r

    # Shifts a block to the left by n bits
    def __shift_left(self, block, n):
        return block[n:] + block[:n]

    # Formats a binary number as a hex string
    def __format_as_hex(self, hex_str):
        hex_str = int(hex_str, 2)  # Convert to base 10
        hex_str = hex(hex_str)  # Convert to base 16
        hex_str = hex_str.upper().replace("0X", "").zfill(16)
        # zfill ensures that the string is 16 characters long
        # If we didn't do this, a hex string with leading zeros would lose them
        return hex_str
