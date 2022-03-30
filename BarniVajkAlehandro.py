f=open("nevezetessegek.txt","r",encoding="utf-8")
mutassad=[]
for sor in f:
    kislista=sor[:-1].split(";")
    mutassad.append(kislista)
f.close()
