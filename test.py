import pytest
from des import DES
from des import triple_DES


# Tests if the plaintext and decrypted ciphertext match
def test_des():
    """Test that the DES implementation is working correctly"""
    key = "133457799BBCDFF1"
    des = DES.DES(key)

    plaintext = "0123456789ABCDEF"
    ciphertext = des.encrypt(plaintext)
    decrypted_text = des.decrypt(ciphertext)

    assert plaintext == decrypted_text


# Tests if the plaintext and decrypted ciphertext match
def test_triple_des_3_keys():
    """Test that the Triple DES implementation is working correctly"""
    key1 = "133457799BBCDFF1"
    key2 = "AABB09182736CCDD"
    key3 = "0E329232EA6D0D73"
    triple_des = triple_DES.TripleDES(key1, key2, key3)

    plaintext = "0123456789ABCDEF"
    ciphertext = triple_des.encrypt(plaintext)
    decrypted_text = triple_des.decrypt(ciphertext)

    assert plaintext == decrypted_text


# Tests if the plaintext and decrypted ciphertext match
def test_triple_des_2_keys():
    """Test that the Triple DES implementation is working correctly"""
    key1 = "133457799BBCDFF1"
    key2 = "AABB09182736CCDD"
    triple_des = triple_DES.TripleDES(key1, key2)

    plaintext = "0123456789ABCDEF"
    ciphertext = triple_des.encrypt(plaintext)
    decrypted_text = triple_des.decrypt(ciphertext)

    assert plaintext == decrypted_text
