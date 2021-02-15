while True:
    n=input("Enter 1 for Enter details or press any key to exit")
    if n=='1':
        class batsman():
            def __init__(self, Name, Age, Matches_played, Runs, No_of_Fours, No_of_sixes):
                self.Name = Name
                self.Age = Age
                self.Matches_played = Matches_played
                self.Runs = Runs
                self.No_of_Fours = No_of_Fours
                self.No_of_sixes = No_of_sixes
            def print(self):
                print("Player Name :",self.Name)
                print("Age of Player is", self.Age)
                print("No. of match played by Player is", self.Matches_played)
                print("Runs of Player is", self.Runs)
                print("No. of Fours hit by player are", self.No_of_Fours)
                print("No. of sixes hit by Player are", self.No_of_sixes)
        Name = str(input("Enter name of Player"))
        Age = int(input("Enter the age of Player"))
        Matches_played = int(input("Enter no. of matches played by player"))
        Runs = int(input("Enter Runs of Players"))
        No_of_Fours = int(input("Enter no. of fours hit by player"))
        No_of_sixes = int(input("Enter no. of sixes hit by player"))        
        S = batsman(Name, Age, Matches_played, Runs, No_of_Fours, No_of_sixes)
        S.print()
    else:
        quit()
