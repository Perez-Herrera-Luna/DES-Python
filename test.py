import pytest
from des import DES
from des import triple_DES


# Tests if the plaintext and decrypted ciphertext match
def test_des():
    """Test that the DES implementation is working correctly"""
    key = "0x133457799bbcdff1"
    des = DES.DES(key)

    plaintext = "0x0123456789abcdef"
    ciphertext = des.encrypt(plaintext)
    decrypted_text = des.decrypt(ciphertext)

    assert plaintext == decrypted_text


# Tests if the plaintext and decrypted ciphertext match
def test_triple_des_3_keys():
    """Test that the Triple DES implementation is working correctly"""
    key = "0x133457799bbcdff1aabb09182736ccdd0e329232ea6d0d73"
    triple_des = triple_DES.TripleDES(key)

    plaintext = "0x0123456789abcdef"
    ciphertext = triple_des.encrypt(plaintext)
    decrypted_text = triple_des.decrypt(ciphertext)

    assert plaintext == decrypted_text


# Tests if the plaintext and decrypted ciphertext match
def test_triple_des_2_keys():
    """Test that the Triple DES implementation is working correctly"""
    key = "0x133457799bbcdff1aabb09182736ccdd"
    triple_des = triple_DES.TripleDES(key)

    plaintext = "0x0123456789abcdef"
    ciphertext = triple_des.encrypt(plaintext)
    decrypted_text = triple_des.decrypt(ciphertext)

    assert plaintext == decrypted_text
