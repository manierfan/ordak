import os
name = input("type a name ?")
x = name = ".txt"
all_files = os.listdir()
if x in all_files:
    print("no you can't ")
else:
    f = open(x, "a")
    f.close()
    print ("done")
        