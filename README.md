# DES-Python

![made-with-python](https://img.shields.io/badge/Made%20with-Python%203-1f425f.svg)
[![license: AGPL-3.0](https://img.shields.io/github/license/Perez-Herrera-Luna/DES-Python.svg)](https://github.com/Perez-Herrera-Luna/DES-Python/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![DES-Python](https://github.com/Perez-Herrera-Luna/DES-Python/actions/workflows/python-app.yml/badge.svg)](https://github.com/Perez-Herrera-Luna/DES-Python/actions/workflows/python-app.yml)
![Unmaintained](http://unmaintained.tech/badge.svg)

Data Encryption Standard (DES) implemented in pure Python

![Demo 2](https://github.com/user-attachments/assets/062b5004-a6c6-4330-bd42-3cc6fc409d5f)

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
Plaintext: 0x0123456789abcdef
Key: 0x133457799bbcdff1
Ciphertext: 0x85e813540f0ab405
Decrypted text: 0x0123456789abcdef
```
Or import the module into your project
```python
from des import DES
```

## Usage

### 1. DES
Define a `DES` object while passing in your key. Key should be a hex string representing an 8 byte hexadecimal number.
```python
from des import DES
des = DES.DES("0x133457799bbcdff1")
```
You can encrypt by calling `encrypt()` and passing in a hex string representing an 8 byte hexadecimal number
```python
des.encrypt("0x0123456789abcdef")    # -> "0x85e813540f0ab405"
```
You can simarly decrypt by calling `decrypt()` and passing in a hex string to decrypt
```python
des.decrypt("0x85e813540f0ab405")    # -> "0x0123456789abcdef"
```

### 2. Triple DES
Much like regular DES you can define a a `TripleDES` object. You must supply a 16 or 24 byte key when creating the object. The appropriate version of Triple DES will be used depending on the key length.
You can call `encrypt()` and `decrypt()` just like regular DES
```python
from des import triple_DES
key = "0x133457799bbcdff1aabb09182736ccdd0e329232ea6d0d73"
triple_des = triple_DES.TripleDES(key)
triple_des.encrypt("0x0123456789abcdef")    # -> "0xec1ba63f85773ab4"
triple_des.encrypt("0xec1ba63f85773ab4")    # -> "0x0123456789abcdef"
```
