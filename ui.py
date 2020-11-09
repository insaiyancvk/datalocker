import string
from encryption_functions import *
def encrypter(cypher_text,i,d):
    enc_funs={
                "1":enc_fun1(cypher_text),
                "2":enc_fun2(cypher_text),
                "3":enc_fun3(cypher_text),
                "4":enc_fun4(cypher_text,int(d)),
                "5":enc_fun5(cypher_text,3),
                "6":enc_fun6(cypher_text)
            } 
    if i=="1" or i=="5":
        return enc_funs[i][0],enc_funs[i][2]
    else:
        return enc_funs[i][0]


def encryption():
    d=input("enter date of birth (ddmmyyyy) or if your choice is no then enter'no:'")
    # date of birth needs to be checked ---function
    if d.isdigit():
        if len(d)==8:
            print("date of birth is entered")
            print("there are 6 functions listed below ,choose a sequence of functions you would prefer ")
            #information abt all functions
            plain_text=input("enter your plain text:")
            func_seq=input("enter the sequence of your choice:")
            func_seq.replace(" ","")
            cypher_text=plain_text[:]          
            enc_funs={
                "1":enc_fun1(cypher_text),
                "2":enc_fun2(cypher_text),
                "3":enc_fun3(cypher_text),
                "4":enc_fun4(cypher_text,int(d)),
                "5":enc_fun5(cypher_text,3),
                "6":enc_fun6(cypher_text)
            }
            n=0
            a=[]
            for i in func_seq:
                if i=="1":
                    cypher_text,n=encrypter(cypher_text,i,d)
                elif i=="5":
                    cypher_text,a=encrypter(cypher_text,i,d)
                else:
                    cypher_text=encrypter(cypher_text,i,d)
            print(cypher_text,n,a)


           


        else:
            print("invalid")
            encryption()


    else:
        print("no date of birth entered")

def decryption():
    print("enter your key")









n=int(input("enter 1 for encryption \n2 for decryption "))
if n==1:
    encryption()
elif n==2:
    decryption()

