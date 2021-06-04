t=int(input())
names=[]
for i in range(t):
    names.append(input())

for name in names:
    if "a" in name or "e" in name or "o" in name or "i" in name or "u" in name:
        print("Yes")
    else:
        print("No")