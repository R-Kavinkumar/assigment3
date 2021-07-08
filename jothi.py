a=open("word.txt","r")
b=a.read()

c=0
for i in b:
    if i=="J":
        c+="I"
    else:
        c+=i
a.close()
