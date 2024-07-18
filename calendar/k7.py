class jalalicalendar:
    def __init__(self,y=1377,m=12,d=12):
        self.__day=d
        self.__month=m
        self.__year=y


    def getter(self):
        d=int(input("enter day"))
        m=int(input("enter month"))
        y=int(input("enter year"))


    def setterd(self):
        return self.__day
    def setterm(self):
        return self.__month
    def settery(self):
        return self.__year



    def getdate(self):
        date=input("enter date as a string")



    def getmontjname(self):
        monthname=input("enter month name")


#######endofclass

mydate=jalalicalendar()
mydate.getdate()
mydate.getter()
print(mydate.settery())
print(mydate.setterm())
print(mydate.setterd())
mydate.getmonthname()




