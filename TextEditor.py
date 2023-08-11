hist=[]
q=int(input())
s=""
oplst=[]
for i in range(q):
    op=input()
    oplst.append(op)

for i in oplst:
    
    if len(i)==1:
        s=hist.pop()
        
    else:
        oprs=i.split()
        if oprs[0]=="1":
            hist.append(s)
            s=s+oprs[1]
        elif oprs[0]=="2":
            hist.append(s)
            s=s[:-int(oprs[1])]
        elif oprs[0]=="3":
            print(s[int(oprs[1])-1])
