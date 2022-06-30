import json

import json
a = int(input(" how many things you gotta do? "))
c = []
while a > 0 :
    b=input("kar: ")
    h = input ("saat:")
    c.append(b)
    f = open("to-do-list.txt","a")
    f.append(c)
    f.close()


    
    