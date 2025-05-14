# DES-Python

![made-with-python](https://img.shields.io/badge/Made%20with-Python%203-1f425f.svg)
[![license: AGPL-3.0](https://img.shields.io/github/license/Perez-Herrera-Luna/DES-Python.svg)](https://github.com/Perez-Herrera-Luna/DES-Python/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![DES-Python](https://github.com/Perez-Herrera-Luna/DES-Python/actions/workflows/python-app.yml/badge.svg)](https://github.com/Perez-Herrera-Luna/DES-Python/actions/workflows/python-app.yml)
![Unmaintained](http://unmaintained.tech/badge.svg)

Data Encryption Standard (DES) implemented in pure Python

![Demo](https://github.com/user-attachments/assets/dc7d5830-3d71-4a24-a2c4-2e5617c53e9a)

## Installation

Clone the repository and enter the directrory
```bash
git clone https://github.com/Perez-Herrera-Luna/DES-Python.git
cd DES-Python
```
Run `driver.py` for a quick example:
```bash
python driver.py
```
```
Plaintext: 0123456789ABCDEF
Key: 133457799BBCDFF1
Ciphertext: 85E813540F0AB405
Decrypted text: 0123456789ABCDEF
```
Or import the module into your project
```python
from des import DES
```

## Usage

### 1. DES

Define a `DES` object while passing in your key. Key should be a string representing an 8 byte hexadecimal number. There should be no leading "0x"
```python
from des import DES
des = DES.DES("133457799BBCDFF1")
```
You can encrypt by calling `encrypt()` and passing in a string representing an 8 byte hexadecimal number
```python
des.encrypt("0123456789ABCDEF")    # -> "85E813540F0AB405"
```
You can simarly decrypt by calling `decrypt()` and passing in a hex string to decrypt
```python
des.decrypt("85E813540F0AB405")    # -> "0123456789ABCDEF"
```

### 2. Triple DES
Works the same as regular DES except you need to pass in two or three keys when defining the `TripleDES` object. If only two keys are supplied, the first key will be used for the third key.
```python
from des import triple_DES
key1 = "133457799BBCDFF1"
key2 = "AABB09182736CCDD"
key3 = "0E329232EA6D0D73"
triple_des = triple_DES.TripleDES(key1, key2, key3)
triple_des.encrypt("0123456789ABCDEF")    # -> "EC1BA63F85773AB4"
triple_des.encrypt("EC1BA63F85773AB4")    # -> "0123456789ABCDEF"
```
