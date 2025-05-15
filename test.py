# Luna Perez-Herrera
# GNU AGPLv3

import pytest
from des import DES


def test_des():
    key = "0x133457799bbcdff1"
    des = DES.DES(key)

    plaintext = "0x0123456789abcdef"
    ciphertext = des.encrypt(plaintext)
    decrypted_text = des.decrypt(ciphertext)

    assert plaintext == decrypted_text


def test_des_padding():
    key = "0x133457799bbcdff1"
    des = DES.DES(key)

    plaintext = "0x01234567"
    ciphertext = des.encrypt(plaintext)
    decrypted_text = des.decrypt(ciphertext)

    assert plaintext == decrypted_text


def test_des_ecb():
    key = "0x133457799bbcdff1"
    des = DES.DES(key)

    plaintext = "0x0123456789abcdef0123456789abcdef"
    ciphertext = des.encrypt(plaintext)
    decrypted_text = des.decrypt(ciphertext)

    assert plaintext == decrypted_text


def test_des_text():
    key = "0x133457799bbcdff1"
    des = DES.DES(key)

    original_message = "secret message"
    plaintext = original_message.encode("utf-8")
    ciphertext = des.encrypt(plaintext)
    cleartext = des.decrypt(ciphertext)
    cleartext = bytes.fromhex(cleartext[2:]).decode("utf-8")

    assert original_message == cleartext
