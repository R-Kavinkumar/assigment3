class time:
    def __init__(self):
        self.hours=0
        self.minutes=0
    def addtime(self,time1,time2):
        self.hours=time1[0]+time2[0]
        self.minutes=time1[1]+time2[1]
        while self.minutes >60:
            self.hours+=1
            self.hours-=60
        self.displayTime()
        self.displayminute()
        return
    def displayTime(self):
        print(self.hours,"hr",self.minutes,"minutes")
        return
    def displayminute(self):
        self.minutes+=60*self.hours
        print(self.minutes,"minutes")
        return
obj=time()
obj.addtime([1,20],[2,20])