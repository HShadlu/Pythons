f1=open("D:\\text1.txt","r")
f2=open("D:\\text2.txt","w")
z=[ ]
for line in f1:
    for t in line:
        z.append(t)
        if t==" ":
            z.reverse()
            for x in z:
                f2.write(x)
            z.clear()

f2.close()
f1.close()