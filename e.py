n=int(input())
blob=str(input())

#removing bad characters from the blob
#for i in range(n):
#    if blob[i] not in ["c","o","d","e"]:
#        del blob[i]

c=0
o=0
d=0
e=0
for i in range(n):
    if blob[i]=="c":
        c+=1 
    elif blob[i]=="o":
        o+=1 
    elif blob[i]=="d":
        d+=1 
    elif blob[i]=="e":
        e+=1

print(min(c,o,d,e))