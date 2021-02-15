class Time():
    def __init__(self, hours, sec, minutes):
        self.hours = hours
        self.sec = sec
        self.minutes = minutes
    def hour_To_min(self,hours):
        Time = (self.hours)*60
        print ("Time is conveted into minutes", Time, "min")
    def sec_to_min(self,sec):
        Time2 = (self.sec)/60
        print ("Time is conveted into minutes", Time2, "min")
    def min_to_min(self,minutes):
        Time3 = (self.minutes)
        print ("Time is already in minutes so time is ", Time3, "min")        
    def print(self):
        print("Time in hours", self.hours)
        print("Time in sec" ,self.sec)
        print("Time in min" ,self.minutes)
hours = float(input("enter time in hours"))
sec = float(input("enter time in sec"))
minutes = float(input("enter time in min"))
A = Time(hours, sec, minutes)
A.print()
A.hour_To_min(hours)
A.sec_to_min(sec)
A.min_to_min(minutes)

        
        
        
        
        
        
        
        
        
