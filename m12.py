a = int(input ("code meli:"))
sum = 0
mynumber=[]
while a:
    mynumber.append(int(a%10))
    a = int(a/10)
print (mynumber)
for i in range (9,0,-1):
    sum = sum+mynumber[i]*(i+1)
m = sum%11
p = 11-m
if m >2:
    
   

elif m >2:
    
    



