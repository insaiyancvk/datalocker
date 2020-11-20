from .constants import caps, small, num

def dec_fun2(x):
    nstr=''
    for i in range (0,len(x)):
        if i%2==0:
            nstr+=x[int(i)]
    return nstr

def dec_fun3(plain_text):
    nstr= ''
    grpstr=plain_text
    for i in range(len(grpstr)):
        if grpstr[i].isupper():
            if (ord(grpstr[i])%64)-5 >= len(caps):
                nstr+=caps[(ord(grpstr[i])%64)-5+len(caps)-1]
            else:
                nstr+=caps[(ord(grpstr[i])%64)-5-1]
        elif grpstr[i].islower():
            if (ord(grpstr[i])%96)-5 >= len(small):
                nstr+=small[(ord(grpstr[i])%96)-5+len(small)-1]
            else:
                nstr+=small[(ord(grpstr[i])%96)-5-1]
        elif ord(grpstr[i])>47 and ord(grpstr[i])<58:
            if (ord(grpstr[i])%47)-5 >= len(num):
                nstr+=num[(ord(grpstr[i])%47)-5+len(num)-1]
            else:
                nstr+=num[(ord(grpstr[i])%47)-5-1]
        elif ord(grpstr[i])>122:
            nstr+=chr(ord(grpstr[i]))
        else:
            nstr+=chr(ord(grpstr[i]))
    grp=[]
    n=len(plain_text)%5
    grp.append(nstr[:n])
    for i in range(0,len(nstr)-n):
        grp.append(nstr[n+((i)*5):n+((i+1)*5)])
    return ''.join(grp[::-1])

def dec_fun4(a,b):
    nstr=''
    if str(b).isdigit()==False:
            print(-1) 
    else:
        ndob = [int(x) for x in str(b)]
        pt=a
        j=0
        for i in range(len(pt)):
            if pt[i].isupper():
                if (ord(pt[i])%64)-ndob[j] >= len(caps):
                    nstr+=caps[(ord(pt[i])%64)-ndob[j]-len(caps)-1]
                else:
                    nstr+=caps[(ord(pt[i])%64)-ndob[j]-1]
            elif pt[i].islower():
                if (ord(pt[i])%96)-ndob[j] >= len(small):
                    nstr+=small[(ord(pt[i])%96)-ndob[j]-len(small)-1]
                else:
                    nstr+=small[(ord(pt[i])%96)-ndob[j]-1]
            elif ord(pt[i])>47 and ord(pt[i])<58:
                if (ord(pt[i])%47)-ndob[j] >= len(num):
                    nstr+=num[(ord(pt[i])%47)-ndob[j]-len(num)-1]
                else:
                    nstr+=num[(ord(pt[i])%47)-ndob[j]-1]
            else:
                nstr+= pt[i]
            j+=1
            if j==len(ndob):
                j=0
    return ''.join(str(i) for i in nstr)

def selector(plain_text,i,d):
    dec_funs={
                "2":dec_fun2(plain_text),
                "3":dec_fun3(plain_text),
                "4":dec_fun4(plain_text,int(d)),
            } 
    return dec_funs[i]

def decryptor(text, key):
    text = str(text)
    plain_text=text[:]
    if str(key).isdigit():
        for i in ["2","4"]:
            plain_text=selector(plain_text,i,d=key)
        return plain_text
    else:
        return -1 # returns -1 if the key has any non-numeric character

# print("mm:", dec_fun4("tclcbp", 1234))
