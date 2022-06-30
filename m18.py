import json
kar = input ("kar?")
saat= int(input ("saat?"))
a = {
     kar:saat 
}
b = json.dumps (a)
with open("m.json", "w") as myfile :
    myfile.write(b)
   

