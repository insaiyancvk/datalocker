import argparse
from datalocker.core import locker

def main():
    parser = argparse.ArgumentParser(description='args')
    parser.add_argument('-e', type=str, help='name of the csv file to be encrypted', default=None)
    parser.add_argument('-d', type=str, help='ame of the csv file to be decrypted', default=None)
    parser.add_argument('--save-as', type=str, help='name of the file to be saved', default= "save.csv")

    args = parser.parse_args()

    if args.e is not None:
        l = locker(filename = args.e)
        l.encrypt_csv(savename=args.save_as, save = True)

    if args.d is not None:
        l = locker(filename = args.d)
        l.decrypt_csv(savename=args.save_as, save = True)

main()
