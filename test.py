caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['0','1','2','3','4','5','6','7','8','9']

def enc_fun4(plain_text,dob):
    if str(dob).isdigit()==False:
        return -1 # returns -1 if the date of birth has text or special characters
    else:
        ndob = [int(x) for x in str(dob)]
        pt=plain_text
        nstr=''
        j=0
        # o=[]
        for i in range(len(pt)):
            if pt[i].isupper():
                if (ord(pt[i])%64)+ndob[j] >= len(caps):
                    nstr+=caps[(ord(pt[i])%64)+ndob[j]-len(caps)-1]
                else:
                    nstr+=caps[(ord(pt[i])%64)+ndob[j]-1]
            elif pt[i].islower():
                if (ord(pt[i])%96)+ndob[j] >= len(small):
                    nstr+=small[(ord(pt[i])%96)+ndob[j]-len(small)-1]
                else:
                    nstr+=small[(ord(pt[i])%96)+ndob[j]-1]
            elif ord(pt[i])>47 and ord(pt[i])<58:
                if (ord(pt[i])%47)+ndob[j] >= len(num):
                    nstr+=num[(ord(pt[i])%47)+ndob[j]-len(num)-1]
                else:
                    nstr+=num[(ord(pt[i])%47)+ndob[j]-1]
            else:
                nstr+= pt[i]
                j+=1
                if j==len(ndob):
                    j=0
        return [''.join(str(i) for i in nstr),4]

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

print(dec_fun4("Qnuux fxaum",99))