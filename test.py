from datalocker.core import locker

l = locker("dummy.csv")
l.encrypt_csv("tom.csv", save = True)

j = locker("tom.csv")
j.decrypt_csv("jerry.csv", save = True)