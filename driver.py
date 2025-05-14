# Luna Perez-Herrera
# GNU AGPLv3

from des import DES


def main():
    key = "0x133457799bbcdff1"
    des = DES.DES(key)

    plaintext = "0x0123456789abcdef"
    ciphertext = des.encrypt(plaintext)
    decrypted_text = des.decrypt(ciphertext)

    print("Plaintext: " + plaintext)
    print("Key: " + key)
    print("Ciphertext: " + ciphertext)
    print("Decrypted text: " + decrypted_text)


if __name__ == "__main__":
    main()
