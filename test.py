import pytest
from des import DES


# Runs the driver and returns true if e
def test_des():
    """Test that the DES module is working correctly"""
    key = "133457799BBCDFF1"
    des = DES.DES(key)

    plaintext = "0123456789ABCDEF"
    ciphertext = des.encrypt(plaintext)
    decrypted_text = des.decrypt(ciphertext)

    assert plaintext == decrypted_text
