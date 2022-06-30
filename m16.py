phonebook = {
    "arad" : "90112113313",
    "amir" : "09211233223",
    "mani" : "09030503805",
    "nani" : "09112223244",
}
a = phonebook.keys()
b = input ("name?")
if b in a:
    print ("ok")
else :
    c = int(input ("number?"))
    phonebook[b]=[c]
print ("\U0001F602")
print (phonebook) 


    
