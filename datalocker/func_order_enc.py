from .encryption_functions import *

try:
    import os
except ModuleNotFoundError:
    print("os library not found \o/")
    exit()

try:
    import pandas as pd
except ModuleNotFoundError:
    print("Pandas library not found :(")
    exit()

def make_csv(d,k,genstr=[]):
    df = pd.DataFrame() # initialize the pandas dataframe
    dt=[] 
    dt.append(k)
    if len(genstr)!=0:
        for i in genstr:
            dt.append(i)
    df[d]=dt
    df.to_csv("database/{}.csv".format(d),index=False) 

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

def func_encryptor(text):
    invalid_options = ['6','7','8','9','0']

    key=input("Enter any number of digits from 1-5 (eg,1432): ") # input key, The range 1-5 are the encryption functions
    d='' # initializing dob/an 8 digit number
    flag=False # using to check if the user used 5th function
    key=str(key) # explicitly convering key to string

    # for checking invalid key input
    for i in key:
        if i in invalid_options:
            key = input("Please choose the key from 1-5: ")
    
    cypher_text=text[:] # copying plain text to another variable
    keygen=[] # initialize list for storing the generated key
    gen_str=[] # a list to store the generated strings from function 5

    # encryption of plain text begins
    for i in key:
        if i=='1':
            cypher_text, e = encrypter1(cypher_text,i)
            # checking if the third element's corresponding number is a single digit (used for generating a key)
            if len(e)==1:
                keygen.append('10')
                keygen.append(e)
            # checking if the third element's corresponding number is a double digit
            else:
                keygen.append('1')
                keygen.append(e)

        #  --------------------------------------------    
        elif i=='5':
            print("You have chosen the 5th encryption function")
            if len(d)==0:
                d=input("Enter your date of birth (or any random 8 digit number): ")
                dirs = os.listdir("./database")
                while (d+".csv") in dirs:
                    d=input("{} already exists in the database, please try any other 8 digit number: ".format(d))
            n=int(input("Enter the number of strings to be generated: "))
            cypher_text, gen_str = encrypter1(cypher_text,i,d,n)
            keygen.append('5')
            flag=True
        #  --------------------------------------------
        elif i=='4':
            if len(d)==0:
                d=input("Enter your date of birth (or any random 8 digit number): ")
                dirs = os.listdir("./database")
                while (d+".csv") in dirs:
                    d=input("{} already exists in the database, please try any other 8 digit number: ".format(d))
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
            print("Data saved to {}.csv".format(d))
        else:
            n=input("dob entered do you want to save the key to the database?(Y/N)")
            if n.lower()=="y":
                make_csv(d,final_key)
                print("Data saved to {}.csv".format(d))
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
        else:
            print("Invalid option.. exiting.")
            exit()


# func_encryptor("hello world",1245) # an example 