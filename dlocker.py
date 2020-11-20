import argparse
from datalocker.core import locker
from datalocker.func_order_enc import func_encryptor
from datalocker.func_order_dec import func_decryptor


def main():
    """
    fetch arg values from the terminal {
    type = default type
    help = message shown when we write $ python dlocker.py -h      
    }
    """
    parser = argparse.ArgumentParser(description='args')
    parser.add_argument('-e', type=str, help='name of the csv file to be encrypted', default=None)
    parser.add_argument('-d', type=str, help='name of the csv file to be decrypted', default=None)
    parser.add_argument('--save-as', type=str, help='name of the file to be saved', default= "save.csv")
    parser.add_argument('--key', type= int, help='key to unlock', default= None)
    parser.add_argument('-e-str', type=str, help='string to be encrypted', default=None)
    parser.add_argument('-d-str', type=str, help='string to be decrypted', default=None)
    args = parser.parse_args()

    """
    arg definitions

    args.e = filename of the csv file to be encrypted 
    args.d = filename of the csv file to be decrypted\
    args.e_str = string to be encrypted 
    args.d_str = string to be decrypted 
    """

    if args.e is not None:
        l = locker(filename = args.e)
        l.encrypt_csv(savename=args.save_as, save = True, key = args.key)

    if args.d is not None:
        l = locker(filename = args.d)
        l.decrypt_csv(savename=args.save_as, save = True,key = args.key)

    if args.e_str is not None:
        func_encryptor(args.e_str)

    if args.d_str is not None:
        func_decryptor(args.d_str)

main()