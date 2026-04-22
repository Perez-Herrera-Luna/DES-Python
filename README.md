# DES-Python

![made-with-python](https://img.shields.io/badge/Made%20with-Python%203-1f425f.svg)
[![license: AGPL-3.0](https://img.shields.io/github/license/Perez-Herrera-Luna/DES-Python.svg)](https://github.com/Perez-Herrera-Luna/DES-Python/blob/main/LICENSE)
[![DES-Python](https://github.com/Perez-Herrera-Luna/DES-Python/actions/workflows/python-app.yml/badge.svg)](https://github.com/Perez-Herrera-Luna/DES-Python/actions/workflows/python-app.yml)

Data Encryption Standard (DES) implemented in pure Python

![Demo](https://github.com/user-attachments/assets/aaa905df-d924-4d52-80f4-b06390c1b523)

## Installation

Install using your Python package manager of choice:
```bash
pip install des_Py
```

```
Plaintext: 0x0123456789abcdef
Key: 0x133457799bbcdff1
Ciphertext: 0x85e813540f0ab405fdf2e174492922f8
Decrypted text: 0x0123456789abcdef
```

## Usage
### Encrypting Hex Strings
Define a `DES` object while passing in your key. The key can be a hex string or a bytes object.
```python
import des_Py
des = des_Py.DES("0x133457799bbcdff1")
```
You can encrypt by calling `encrypt()` and passing in a hex string or bytes object.
```python
des.encrypt("0x0123456789abcdef")    # -> "0x85e813540f0ab405fdf2e174492922f8"
```
You can simarly decrypt by calling `decrypt()` and passing in a hex string or bytes object.
```python
des.decrypt("0x85e813540f0ab405fdf2e174492922f8")    # -> "0x0123456789abcdef"
```
