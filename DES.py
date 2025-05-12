# Luna Perez-Herrera
# GNU AGPLv3

import Constants


class DES:
    def __init__(self, key: str):
        # Key should be a 64 bit hexadexcimal string with no leading '0x'
        self.key = bin(int(key, 16))[2:].zfill(64)

        self.PC1 = Constants.des_PC1()
        self.PC2 = Constants.des_PC2()
        self.shifts = Constants.des_shifts()
        self.IP = Constants.des_IP()
        self.FP = Constants.des_FP()
        self.EP = Constants.des_EP()
        self.PF = Constants.des_PF()
        self.sboxes = Constants.des_sboxes()
        self.round_keys = self.generate_round_keys()
        self.round_keys_reversed = self.round_keys[::-1]

    def encrypt(self, plaintext: str) -> str:
        # Plaintext should be a 64 bit hexadecimal string with no leading '0x'
        plaintext = bin(int(plaintext, 16))[2:].zfill(64)

        # Preform initial permutation
        plaintext = self.permute(plaintext, self.IP)

        # Split into two halves
        L = [plaintext[:32]]
        R = [plaintext[32:]]

        # Perform 16 rounds of DES
        for i in range(16):
            L.append(R[i])
            R.append(self.xor(L[i], self.f(R[i], self.round_keys[i])))

        # Preform final permutation
        ciphertext = self.permute(R[16] + L[16], self.FP)

        return self.format_as_hex(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        # Ciphertext should be a 64 bit hexadecimal string with no leading '0x'
        ciphertext = bin(int(ciphertext, 16))[2:].zfill(64)

        # Perform intial permutation
        ciphertext = self.permute(ciphertext, self.IP)

        # Split into two halves
        L = [ciphertext[:32]]
        R = [ciphertext[32:]]

        # Perform 16 rounds of DES
        for i in range(16):
            L.append(R[i])
            R.append(self.xor(L[i], self.f(R[i], self.round_keys_reversed[i])))

        # Preform final permutation
        cleartext = self.permute(R[16] + L[16], self.FP)

        return self.format_as_hex(cleartext)

    # Generates the 16 rounds keys used in DES
    def generate_round_keys(self):
        # Apply PC-1
        temp_key = self.permute(self.key, self.PC1)

        # Split into two halves
        c_keys = [temp_key[:28]]
        d_keys = [temp_key[28:]]

        # Generate 16 'c' and 'd' keys
        for i in range(16):
            c_keys.append(self.shift_left(c_keys[i], self.shifts[i]))
            d_keys.append(self.shift_left(d_keys[i], self.shifts[i]))

        # List to store round keys
        round_keys = []

        # Append 'c' and 'd' keys to form round keys
        for i in range(1, 17):
            key_i = c_keys[i] + d_keys[i]
            round_keys.append(self.permute(key_i, self.PC2))  # Permute with PC-2

        return round_keys

    # Permutes the input according to the table. Used for all the fancy permutations in DES
    def permute(self, key, table):
        permuted_key = ""

        # Permute the key according to the table
        for i in table:
            permuted_key += key[i - 1]
            # The -1 is because all the tables are 1-indexed, but arrays are 0-indexed

        return permuted_key

    # Preforms the S-box substitution in the DES algorithm
    def s_box_substitution(self, R):
        # Split into 8 blocks of 6 bits
        blocks = [R[i : i + 6] for i in range(0, len(R), 6)]

        # Perform S-box substitution
        for i, block in enumerate(blocks):
            row = int(block[0] + block[5], 2)  # First and last bit
            col = int(block[1:5], 2)  # Middle 4 bits
            blocks[i] = format(self.sboxes[i][row][col], "04b")  # Format to 4 bits

        # Concatenates the blocks. Think of this as flattening the list
        return "".join(blocks)

    # Preforms the XOR operation on two binary strings
    def xor(self, a, b):
        # XORs each bit one by one
        return "".join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    # Preforms the f function in the DES algorithm
    def f(self, R, input):
        # Perform expansion permutation
        R = self.permute(R, self.EP)

        # XOR with input
        R = self.xor(R, input)

        # Perform S-box substitution
        R = self.s_box_substitution(R)

        # Perform permutation
        R = self.permute(R, self.PF)

        return R

    # Shifts an input to the left by n bits
    def shift_left(self, input, n):
        return input[n:] + input[:n]

    # Formats a binary number as a hex string
    def format_as_hex(self, hex_str):
        hex_str = int(hex_str, 2)  # Convert to base 10
        hex_str = hex(hex_str)  # Convert to base 16
        hex_str = hex_str.upper().replace("0X", "").zfill(16)
        # zfill ensures that the string is 16 characters long. Fixes issues where the hex has leading zeros
        # If we didn't do this, a hex string with leading zeros would lose them
        return hex_str
