f1=open("D:\\text1.txt","w")

r=2
def  calcx(n):
    if n==0:
     return 0.2
    else:
      return calcx(n-1)*r * (1-calcx(n-1))




while r<=4:
    z=calcx(500)
    f1.write(str(z)+"\n")
    r=r+0.01



