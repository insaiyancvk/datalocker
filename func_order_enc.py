from encryption_functions import *

try:
    import pandas as pd
except:
    print("Pandas library not found :(")
    exit()

def make_csv(d,k,genstr=[]):
    try:
        df = pd.read_csv("db.csv")
        print("Reading the database")
        dt=[]
        dt.append(k)
        for i in genstr:
            dt.append(i)
        df[d]=dt
        df.to_csv("db.csv",index=False)
    except:
        dt=[]
        dt.append(k)
        for i in genstr:
            dt.append(i)
        data={
            d:dt
        }
        df = pd.DataFrame(data)
        df.to_csv("db.csv",index=False)

def encrypter1(cypher_text,i,d=0,n=0):
    enc_funs={
                "1":enc_fun1(cypher_text),
                "2":enc_fun2(cypher_text),
                "3":enc_fun3(cypher_text),
                "4":enc_fun4(cypher_text,int(d)),
                "5":enc_fun5(cypher_text,n),
                "6":enc_fun6(cypher_text)
            } 
    if i=="1":
        return enc_funs[i][0],str(enc_funs[i][2])
    elif i=="5":
        return enc_funs[i][0],enc_funs[i][2]
    else:
        return enc_funs[i][0]

def func_encryptor(text, key):
    d=''
    flag=False
    key=str(key)
    cypher_text=text[:]
    keygen=[]
    gen_str=[]
    for i in key:
        if i=='1':
            cypher_text, e = encrypter1(cypher_text,i)
            if len(e)==1:
                keygen.append('10')
                keygen.append(e)
            else:
                keygen.append('1')
                keygen.append(e)
        elif i=='5':
            print("You have chosen the 5th encryption function")
            if len(d)==0:
                d=input("Enter your date of birth (or any random 8 digit number): ")
                try:
                    df = pd.read_csv("db.csv")
                    while d in df.columns:
                        d=input("{} already exists in the database, please try any other 8 digit number: ".format(d))
                except:
                    pass
            n=int(input("Enter the number of strings to be generated: "))
            cypher_text, gen_str = encrypter1(cypher_text,i,d,n)
            keygen.append('5')
            flag=True
        elif i=='4':
            if len(d)==0:
                d=input("Enter your date of birth (or any random 8 digit number): ")
                try:
                    df = pd.read_csv("db.csv")
                    while d in df.columns:
                        d=input("{} already exists in the database, please try any other 8 digit number: ".format(d))
                except:
                    pass
            cypher_text = encrypter1(cypher_text,i,d)
            keygen.append('4')
        else:
            cypher_text = encrypter1(cypher_text,i)
            keygen.append(i)
    print()
    print("- "*45)
    print("Here is your encrypted text: {}\n".format(cypher_text))
    final_key = ''.join(str(i) for i in keygen)
    print("Here is the key: ", final_key)
    print("- "*45)
    print()
    if len(d)!=0:
        if flag:
            print("Saving the generated strings to the database.. ")
            make_csv(d,final_key,gen_str)
            print("Data saved to db.csv")
        else:
            n=input("dob entered do you want to save the key to the database?(Y/N)")
            if n.lower()=="y":
                make_csv(d,final_key)
                print("Data saved to db.csv")
            elif n.lower()=='n':
                print("\nPlease remember the key :)\n")
    else:
        yn=input("Would you like to save your key into the database?(Y/N): ")
        if yn.lower()=='y':
            d=int(input("Enter your date of birth(or any 8 digit number): "))
            make_csv(d,final_key)
            print("\nSuccessfully saved to the database\n")
        elif yn.lower()=='n':
            print("Please remember the key :)\n")


func_encryptor("Hello world",123)