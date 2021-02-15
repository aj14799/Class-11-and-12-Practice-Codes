while True:
    a = input("Enter 1 To Continue or press any key to Exit:")
    if a=='1':
        class Play():
            def __init__(self):
                self.PlayCode = 0
                self.PlayTitle = None
                self.Duration = 45 
                self.NoOfScenes = 5
            def NewPlay(self):
                n = input("Enter 1 for Chage play durations or No. of Scenes")
                if n=='1':
                    self.Duration = float(input("Enter New Duration in minutes "))
                    self.NoOfScenes = int(input("Enter New no. of Scenes"))
                else:
                    self.Duration = self.Duration
                    self.NoOfScenes = self.NoOfScenes
            def Moreinfo(self):
                self.PlayCode = int(input("Enter Play Code:")) 
                self.PlayTitle = str(input("Enter Play Title:"))
            def show(self):
                print("Title:", self.PlayTitle )
                print("Play Code:", self.PlayCode)
                print("Duration:",self.Duration, "minutes" )
                print("No. of Scenes", self.NoOfScenes)
                
        P=Play()
        P.Moreinfo()
        P.NewPlay()
        P.show()
    else:
        exit()
