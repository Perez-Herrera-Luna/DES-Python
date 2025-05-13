# Luna Perez-Herrera
# GNU AGPLv3

from des import DES


def main():
    key = "133457799BBCDFF1"
    des = DES.DES(key)

    plaintext = "0123456789ABCDEF"
    ciphertext = des.encrypt(plaintext)
    decrypted_text = des.decrypt(ciphertext)

    print("Plaintext: " + plaintext)
    print("Key: " + key)
    print("Ciphertext: " + ciphertext)
    print("Decrypted text: " + decrypted_text)


if __name__ == "__main__":
    main()
