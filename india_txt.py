opener=open("word.txt","r")
reader=opener.read().split(" ")
opener.close()
count=0
for i in range(len(reader)):
    if reader[i]=="INDIA":
        count+=1
print(count)