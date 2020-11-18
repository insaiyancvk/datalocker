import pandas as pd 
from .encryption_functions import enc_fun2
from .decryption_functions import dec_fun2

class locker(object):
    def __init__(self, filename):

        self.csv = pd.read_csv(filename)
        self.old_shape = self.csv.values.shape

    def encrypt_csv(self,savename = "enc.csv", save = False):
        flat = self.csv.values.flatten()

        for i in range(len(flat)):
            flat[i] = enc_fun2(flat[i])
        e = flat.reshape(self.old_shape)
        df_encrypted = pd.DataFrame(e, columns = self.csv.columns)

        if save is True:
            df_encrypted.to_csv(savename, index = False)

        return df_encrypted

    def decrypt_csv(self, savename = "dec.csv", save = False):
        flat = self.csv.values.flatten()

        for i in range(len(flat)):
            flat[i] = dec_fun2(flat[i])
        e = flat.reshape(self.old_shape)
        df_encrypted = pd.DataFrame(e, columns = self.csv.columns)

        if save is True:
            df_encrypted.to_csv(savename, index = False)

        return df_encrypted


