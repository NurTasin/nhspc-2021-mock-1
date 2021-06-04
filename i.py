def listify(string):
    lstring=[]
    for i in range(len(string)):
        lstring.append(string[i])
    return lstring

t=int(input())

strings=[]
args=[]

for i in range(t):
    strings.append(str(input()))
    args.append(str(input()))

for i in range(t):
    string=strings[i]
    blanks=string.count("?")
    argc=int(args[i].split(" ")[0])
    nominees=str(args[i].split(" ")[1])
    list_of_nominee=listify(nominees)
    list_of_nominee.sort()
    count=0
    nstr=""
    for j in range(len(string)):
        if string[j]=='?':
            if argc!=blanks:
                nstr+="".join(list_of_nominee)
            else:
                nstr+=list_of_nominee[count]
            count+=1
        else:
            nstr+=string[j]
    
    print(nstr)