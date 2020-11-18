from .constants import caps, small, num

def dec_fun2(x):
    nstr=''
    for i in range (0,len(x)):
        if i%2==0:
            nstr+=x[int(i)]
    return nstr
