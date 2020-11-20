# Datalocker

Use it to easily encrypt/decrypt csv files.

## Getting started

1. `git clone https://github.com/insaiyancvk/OOPminiProject.git`

2. `cd OOPminiProject`

## Arguments

```
  -h, --help         show this help message and exit
  -e E               name of the csv file to be encrypted saved
  --key KEY          key to unlock
  -e-str E_STR       string to be encrypted
  -d-str D_STR       string to be decrypted
```

## Utilities

To encrypt a file with a key:
```
python dlocker.py  -e carssales.csv --save-as encrypted.csv --key 1234
```

To decrypt a file with a key:
```
python dlocker.py  -d encrypted.csv --save-as decrypted.csv --key 1234
```

To encrypt a string:
```
python dlocker.py -e-str hello
```

To decrypt a string:
```
python dlocker.py -d-str encrypted_string
```

For help:
```
python dlocker.py --help
```
