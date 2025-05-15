# Luna Perez-Herrera
# GNU AGPLv3

"""Module providing a DES implementation for encryption"""

from des import constants


class DES:
    """Class for a DES object. Capable of encrypting or decrypting an input with a key"""

    def __init__(self, key):
        # Key should be a hex string or bytes object
        if self.__is_bytes_object(key):
            key = self.__bytes_object_to_hex(key)

        self.__validate_key(key)
        self.key = self.__format_key(key)

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

    def encrypt(self, plaintext) -> str:
        """Encrypts the input plaintext by the key"""
        # Plaintext should be a hex string or bytes object
        if self.__is_bytes_object(plaintext):
            plaintext = self.__bytes_object_to_hex(plaintext)

        self.__validate_input(plaintext)
        plaintext = self.__format_input(plaintext)
        blocks = self.__split_blocks_encrypt(plaintext)
        blocks[-1] = self.__pad_block(blocks[-1])

        ciphertext = []
        for block in blocks:
            ciphertext.append(self.__encrypt_block(block))

        return "0x" + "".join(ciphertext)

    def decrypt(self, ciphertext) -> str:
        """Decryptes the input ciphertext by the key"""
        # Ciphertext should be a hex string or bytes object
        if self.__is_bytes_object(ciphertext):
            ciphertext = self.__bytes_object_to_hex(ciphertext)

        self.__validate_input(ciphertext)
        self.__validate_ciphertext(ciphertext)
        ciphertext = self.__format_input(ciphertext)
        blocks = self.__split_blocks_decrypt(ciphertext)

        cleartext = []
        for block in blocks:
            cleartext.append(self.__decrypt_block(block))

        cleartext[-1] = self.__strip_padding(cleartext[-1])

        return "0x" + "".join(cleartext)

    def __encrypt_block(self, plaintext: str) -> str:
        plaintext = self.__format_block(plaintext)

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

        return self.__format_binary_string_as_hex(ciphertext)

    def __decrypt_block(self, ciphertext: str) -> str:
        ciphertext = self.__format_block(ciphertext)

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

        return self.__format_binary_string_as_hex(cleartext)

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
    def __format_binary_string_as_hex(self, hex_str):
        hex_str = int(hex_str, 2)  # Converts to base 10
        hex_str = hex(hex_str)[2:].zfill(16)

        return hex_str

    def __format_input(self, input_string: str):
        input_string = input_string.lower()

        if "0x" in input_string[:2]:
            input_string = input_string[2:]

        if len(input_string) % 2 == 1:
            input_string = "0" + input_string

        return input_string

    def __format_block(self, block: str) -> str:
        return bin(int(block, 16))[2:].zfill(64)

    def __format_key(self, key: str) -> str:
        return bin(int(key, 16))[2:].zfill(64)

    def __bytes_object_to_hex(self, bytes_array: bytes) -> str:
        return bytes_array.hex()

    def __is_bytes_object(self, bytes_object) -> bool:
        if isinstance(bytes_object, bytes):
            return True
        else:
            return False

    # Validates key, cleartext, and ciphertext input
    def __validate_key(self, key: str):
        if not isinstance(key, str):
            raise TypeError(
                "Invalid key type. Key should be a hex string or a bytes objects"
            )

        key = key.lower()

        if "0x" in key[:2]:
            key = key[2:]

        if len(key) != 16:
            raise ValueError("Key is of incorrect length")

        self.__validate_hex_string(key)

    def __validate_hex_string(self, hex_string: str):
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
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
        }

        for char in hex_string:
            if char not in valid_set:
                raise ValueError(
                    "Invalid hex string. Characters in string should be 0-f"
                )

    def __validate_input(self, input_string: str):
        if not isinstance(input_string, str):
            raise TypeError(
                "Invalid input type. Input should be a hex string or a bytes objects"
            )

        input_string = input_string.lower()

        if "0x" in input_string[:2]:
            input_string = input_string[2:]

        self.__validate_hex_string(input_string)

    def __validate_ciphertext(self, ciphertext: str):
        ciphertext = ciphertext.lower()

        if "0x" in ciphertext[:2]:
            ciphertext = ciphertext[2:]

        if not len(ciphertext) % 16 == 0:
            raise ValueError("Decryption input is not multiple of block size (8 bytes)")

    def __split_blocks_encrypt(self, input_string: str) -> list[str]:
        n = len(input_string)
        num_blocks = n // 16
        remainder = n % 16

        blocks = []
        for i in range(num_blocks):
            blocks.append(input_string[16 * i : 16 * (i + 1)])

        if remainder == 0:
            blocks.append("")
        else:
            blocks.append(input_string[16 * num_blocks : n])

        return blocks

    def __split_blocks_decrypt(self, input_string: str) -> list[str]:
        n = len(input_string)
        num_blocks = n // 16

        blocks = []
        for i in range(num_blocks):
            blocks.append(input_string[16 * i : 16 * (i + 1)])

        return blocks

    def __pad_block(self, input_string: str) -> str:
        full_block = 16
        n = len(input_string)
        pad_length = (full_block - n) // 2

        pad_character = "0" + str(pad_length)
        for _ in range(pad_length):
            input_string += pad_character

        return input_string

    def __strip_padding(self, input_string: str) -> str:
        strip_length = int(input_string[14:16], 16)

        if strip_length > 8 or strip_length < 1:
            # Invalid strip_length
            return input_string

        for i in range(16 - (strip_length * 2), 16, 2):
            if int(input_string[i : i + 2], 16) != strip_length:
                return input_string

        return input_string[0 : 16 - (strip_length * 2)]
