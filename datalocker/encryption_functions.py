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

