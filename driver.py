# Luna Perez-Herrera
# GNU AGPLv3

import des_PurePy


def main():
    key = "0x133457799bbcdff1"
    des1 = des_PurePy.DES(key)

    plaintext = "0x0123456789abcdef"
    ciphertext = des1.encrypt(plaintext)
    decrypted_text = des1.decrypt(ciphertext)

    print("Plaintext: " + plaintext)
    print("Key: " + key)
    print("Ciphertext: " + ciphertext)
    print("Decrypted text: " + decrypted_text)


if __name__ == "__main__":
    main()
