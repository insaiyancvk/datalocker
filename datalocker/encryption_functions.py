import random, string
from .constants import caps, small, num

def enc_fun2(plain_text):

    if type(plain_text) == int:
        """
        force convert int to str
        """
        plain_text = str(plain_text)

    nstr=''
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(len(plain_text)))
    for i in range(0,2*len(plain_text)):
        if i%2==0:
            if i>=len(plain_text):
                nstr+= plain_text[int(i/2)-len(plain_text)]
            else:
                nstr+= plain_text[int(i/2)]
        else:
            if i>=len(x):
               nstr+= x[int(i/2)-len(plain_text)]
            else:
                nstr+= x[int(i/2)]
    return nstr

def enc_fun3(plain_text):
    grp=[]
    n=(len(plain_text))%5
    for i in range(0,int((len(plain_text))/5)):
        grp.append(plain_text[i*5:(i+1)*5])
        if i==int((len(plain_text)-1)/5)-1:
            grp.append(plain_text[(i+1)*5:((i+1)*5)+n])

    grpstr = ''.join(grp[::-1])
    nstr=''
    for i in range(len(grpstr)):
        if grpstr[i].isupper():
            if (ord(grpstr[i])%64)+5 >= len(caps):
                nstr+=caps[(ord(grpstr[i])%64)+5-len(caps)-1]
            else:
                nstr+=caps[(ord(grpstr[i])%64)+5-1]
        elif grpstr[i].islower():
            if (ord(grpstr[i])%96)+5 >= len(small):
                nstr+=small[(ord(grpstr[i])%96)+5-len(small)-1]
            else:
                nstr+=small[(ord(grpstr[i])%96)+5-1]
        elif ord(grpstr[i])>47 and ord(grpstr[i])<58:
            if (ord(grpstr[i])%47)+5 >= len(num):
                nstr+=num[(ord(grpstr[i])%47)+5-len(num)-1]
            else:
                nstr+=num[(ord(grpstr[i])%47)+5-1]
        elif ord(grpstr[i])>122:
            nstr+=chr(ord(grpstr[i]))
        else:
            nstr+=chr(ord(grpstr[i]))
    return [nstr,3]

def enc_fun4(plain_text,dob):
    if str(dob).isdigit()==False:
        return -1 # returns -1 if the date of birth has text or special characters
    else:
        ndob = [int(x) for x in str(dob)]
        pt=plain_text
        j=0
        o=[]
        for i in range(len(pt)):
            if ord(pt[i])>=123:
                o.append(pt[i])
            else:
                o.append(chr(ord(pt[i])+ndob[j]))
            j+=1
            if j==len(ndob):
                j=0
        return [''.join(str(i) for i in o),4]

def selector(cypher_text,i,d):
    enc_funs={
                "2":enc_fun2(cypher_text),
                "3":enc_fun3(cypher_text),
                "4":enc_fun4(cypher_text,int(d))
            } 
    return enc_funs[i][0]

def encryptor(text, key):
    cypher_text=text[:]
    if str(key).isdigit():
        for i in ["3","4"]:
            cypher_text=selector(cypher_text,i,d=key)
        return cypher_text
    else:
        return -1 # returns -1 if the key has any non-numeric character

# print(encryptor("Hello ~!@#$123",104587))
