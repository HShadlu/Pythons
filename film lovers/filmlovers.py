
thisdict = {
  "Action": 0,
  "Adventure": 0,
  "Comedy": 0,
  "History": 0,
  "Horror": 0,
  "Romance": 0

}

n=int(input())
for i in range (n):
    Horrorf = 1
    Romancef = 1
    Comedyf = 1
    Historyf = 1
    Adventuref = 1
    Actionf = 1
    data = input()
    list = data.split()
    for x in list:
        if(x=="Horror"):
                  if(Horrorf):
                       thisdict["Horror"]+=1
                       Horrorf=0
        if (x == "Romance"):
            if (Romancef):
                thisdict["Romance"]+= 1
                Romancef = 0

        if (x == "Comedy"):
            if (Comedyf):
               thisdict["Comedy"]+= 1
               Comedyf = 0

        if (x == "History"):
            if (Historyf):
                thisdict["History"] += 1
                Historyf = 0

        if (x == "Adventure"):
            if (Adventuref):
                thisdict["Adventure"] += 1
                Adventuref = 0

        if (x == "Action"):
            if (Actionf):
                thisdict["Action"] += 1
                Actionf = 0
#print(thisdict)
maxval=0
for i in range(6):
  for j in thisdict:
    if(thisdict[j]>maxval):
      maxval=thisdict[j]
      maxdata=j

  if(maxval>0):
    print(maxdata," : ",maxval)
    maxval=0
    thisdict.pop(maxdata)



for j in thisdict:
    print(j," : 0")

