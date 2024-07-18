f1=open("D:\\text1.txt","r")
f2=open("D:\\text2.txt","a")
for line in f1:
  f2.write(line)

f2.close()
f1.close()



