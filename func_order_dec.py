from decryption_functions import *
from itertools import islice
try:
    import pandas as pd
except:
    print("Pandas library not found :(")
    exit()

def decrypter1(cypher_text,i,n=0,d='0',gen_str=[]):
    if i=='1':
        return dec_fun1(cypher_text,n)
    elif i=='2':
        return dec_fun2(cypher_text)
    elif i=='3':
        return dec_fun3(cypher_text)
    elif i=='4':
        return dec_fun4(cypher_text,int(d))
    elif i=='5':
        return dec_fun5(cypher_text,gen_str)
    elif i=='6':
        return dec_fun6(cypher_text)
    # dec_funs={
    #             "2":dec_fun2(cypher_text),
    #             "3":dec_fun3(cypher_text),
    #             "6":dec_fun6(cypher_text),
    #             "4":dec_fun4(cypher_text,int(d)),
    #             "5":dec_fun5(cypher_text,gen_str),
    #             "1":dec_fun1(cypher_text,n)
    #         } 
    # return dec_funs[i]
    
def func_decryptor(text,key=''):
    d=''
    x = input("Is your data saved in the database?\nif it is, then the key will automatically be loaded(Y/N): ")
    if x.lower()=='y':
        try:
            df = pd.read_csv("db.csv")
            print("database successfully loaded")
            d=input("Enter your dob/the '8 digit' number: ")
            try:
                strs=df[d]
                key=strs[0]
                print("Your key: {}\n".format(key))
            except:
                print("dob/the number not found in the database :(")
                key=input("Enter the key: ")
        except FileNotFoundError:
            print("Database not found :(")
    elif x.lower()=='n':
        key=input("Enter the key: ")
    key=str(key)
    order=[]
    plain_text=text[:]
    i=0
    while i<len(key):
        if key[i]=='1':
            temp=key[i]+key[i+1:i+3]
            order.append(temp)
            i+=3
        else:
            order.append(key[i])
            i+=1
    order=order[::-1]
    for i in order:
        if len(i)==3:
            plain_text=decrypter1(plain_text,i[0],int(i[1:3]))
        elif i=='4':
            if len(d)==0:
                d=input("Enter your dob (or the random 8 digit number) \nthat you entered while encryption: ")
            if d.isdigit()==True:
                plain_text = decrypter1(plain_text,i,d)
            else:
                print("Non-numeric characters detected")
                exit()
        elif i=='5':
            if len(d)==0:
                d=input("Enter your dob (or the random 8 digit number) \nthat you entered while encryption: ")
            if d.isdigit()==True:
                try:
                    df = pd.read_csv("db.csv",index_col=None)
                    # try:
                    if len(strs)==0:
                        strs = df[d]
                    if len(strs)!=2:
                        print("Key or generated strings missing :(")
                        exit()
                    print(strs[1])
                    plain_text = decrypter1(plain_text,i,d,gen_str=strs[1])
                    # except Exception as e:
                    #     print("\ndob/your '8 digit number' not found the the database :(")
                    #     print(e)
                    #     exit()
                except FileNotFoundError:
                    print("Database not found :(\n")
                    exit()
            else:
                print("Non-numeric characters detected")
        else:
            plain_text = decrypter1(plain_text,i)
    
func_decryptor("b rismQwlry")
        