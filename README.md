# DES-Python

![made-with-python](https://img.shields.io/badge/Made%20with-Python%203-1f425f.svg)
[![license: AGPL-3.0](https://img.shields.io/github/license/Perez-Herrera-Luna/DES-Python.svg)](https://github.com/Perez-Herrera-Luna/DES-Python/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![DES-Python](https://github.com/Perez-Herrera-Luna/DES-Python/actions/workflows/python-app.yml/badge.svg)](https://github.com/Perez-Herrera-Luna/DES-Python/actions/workflows/python-app.yml)
![Unmaintained](http://unmaintained.tech/badge.svg)

Data Encryption Standard (DES) implemented in pure Python

![Demo 3](https://github.com/user-attachments/assets/f2e17c10-1e13-4f43-8b27-618ed0468fc4)

## Features

- **Encryption and Decryption**
- **PKCS5 Padding**
- **ECB Mode of Operation**
- **Hex String and Bytes Object Support**

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
Ciphertext: 0x85e813540f0ab405fdf2e174492922f8
Decrypted text: 0x0123456789abcdef
```
Or import the module into your project
```python
from des import DES
```

## Usage
### Encrypting Hex Strings
Define a `DES` object while passing in your key. The key can be a hex string or a bytes object.
```python
from des import DES
des = DES.DES("0x133457799bbcdff1")
```
You can encrypt by calling `encrypt()` and passing in a hex string or bytes object.
```python
des.encrypt("0x0123456789abcdef")    # -> "0x85e813540f0ab405fdf2e174492922f8"
```
You can simarly decrypt by calling `decrypt()` and passing in a hex string or bytes object.
```python
des.decrypt("0x85e813540f0ab405fdf2e174492922f8")    # -> "0x0123456789abcdef"
```
By default, encryption input is padded to a multiple of the block size (8 bytes) according to PKCS5. Inputs that are multiple blocks long are encrypted using the Electronic Code Book (ECB) mode of operation.
### Encrypting Bytes Objects and Text
Inputs can be hex strings or bytes objects. The key must always be 8 bytes but the encryption input can have any size. 
Because of the bytes object support, with some work, you can encrypt and decrypt text.
```python
key = b"password"
des = DES.DES(key)

ciphertext = des.encrypt(b"secret message")                 # -> "0x0d417ca7d23582bab5e2c9277f801591"
cleartext = des.decrypt(ciphertext)                         # -> "0x736563726574206d657373616765"
cleartext = bytes.fromhex(cleartext[2:]).decode("utf-8")    # -> "secret message"
```
Note that all input is validated so if you passing in an inapropriate input the module will raise a corresponding error.
