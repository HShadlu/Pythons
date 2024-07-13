mylist = eval(input())
min=mylist[0][0]
row=-1
col=-1
for x in mylist:
   row+=1
   for j in x :

       col+=1

       if(j<=min):
           min=j;
           minrow=row
           mincol=col

   col=-1


del mylist[minrow]
for x in mylist:
    del x[mincol]


print(mylist)



