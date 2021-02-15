1#Class Batsman
while True:
    n=input("Enter 1 for Enter details or press any key to exit")
    if n=='1':
        class batsman():
            def __init__(self, Name=None, Age=0, Matches_played=0, Runs=0, No_of_Fours=0, No_of_sixes=0):
                self.Name = str(input("Enter name of Player"))
                self.Age = int(input("Enter the age of Player"))
                self.Matches_played = int(input("Enter no. of matches played by player"))
                self.Runs = int(input("Enter Runs of Players"))
                self.No_of_Fours = int(input("Enter no. of fours hit by player"))
                self.No_of_sixes = int(input("Enter no. of sixes hit by player"))
            def print(self):
                print("Player Name :",self.Name)
                print("Age of Player is", self.Age)
                print("No. of match played by Player is", self.Matches_played)
                print("Runs of Player is", self.Runs)
                print("No. of Fours hit by player are", self.No_of_Fours)
                print("No. of sixes hit by Player are", self.No_of_sixes)  
        S = batsman(Name=None, Age=0, Matches_played=0, Runs=0, No_of_Fours=0, No_of_sixes=0)
        S.print()
    else:
        quit()

        
