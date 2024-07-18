
f1=open("D:\\text1.txt","r")
n=0
for line in f1:
  for char in line:
    if char==" ":

        n=n+1

print(n)
f1.close()


