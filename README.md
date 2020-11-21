# Datalocker :lock:

Use it to easily encrypt/decrypt csv files.

## Getting started :closed_book:

Install required libraries

  0. `pip install pandas argparse`

Clone the repo

  1. `git clone https://github.com/insaiyancvk/datalocker.git`

Navigate into the folder

  2. `cd datalocker`

## Arguments 

```
  -h, --help         show this help message and exit
  -e E               name of the csv file to be encrypted saved
  --key KEY          key to unlock
  -e-str E_STR       string to be encrypted
  -d-str D_STR       string to be decrypted
```

## Utilities :wrench:

To encrypt a file with a key:
```
python dlocker.py  -e carsales.csv --save-as encrypted.csv --key 1234
```

To decrypt a file with a key:
```
python dlocker.py  -d encrypted.csv --save-as decrypted.csv --key 1234
```

To encrypt a string:
```
python dlocker.py -e-str <string>
```

To decrypt a string:
```
python dlocker.py -d-str <encrypted_string>
```

For help:
```
python dlocker.py --help
```

## Use these encryption/decryption functions in your project!

0. `pip install pandas argparse`
1. `git clone https://github.com/insaiyancvk/datalocker.git`
2. In your project, import the functions file:
    * For the encryption functions:

      `from  datalocker.encryption_functions import enc_fun1,enc_fun2,enc_fun3,enc_fun4` 
    
    * For the decryption functions:

      `from  datalocker.decryption_functions import dec_fun1, dec_fun2, dec_fun3, dec_fun4`