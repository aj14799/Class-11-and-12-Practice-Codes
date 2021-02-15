while True:
    n=input("Enter 1 for Enter details or press any key to exit")
    if n=='1':
        class batsman():
            def __init__(self, Name=None, Age=0, Matches_played=0, Wickets=0, Avg_Speed=0, Over=0):
                self.Name = str(input("Enter name of Player"))
                self.Age = int(input("Enter the age of Player"))
                self.Matches_played = int(input("Enter no. of matches played by player"))
                self.Wickets = int(input("Enter Wickets taken of Players"))
                self.Avg_Speed = float(input("Enter avg Speed of player"))
                self.Over = float(input("Enter no. of overs balled by player"))
            def print(self):
                print("Player Name :",self.Name)
                print("Age of Player is", self.Age)
                print("No. of match played by Player is", self.Matches_played)
                print("Wickets taken Player is", self.Wickets)
                print("Avg. Balling Speed of player", self.Avg_Speed)
                print("No. of Overs by Player", self.Over)  
        S = batsman(Name=None, Age=0, Matches_played=0, Wickets=0, Avg_Speed=0, Over=0)
        S.print()
    else:
        quit()

        
