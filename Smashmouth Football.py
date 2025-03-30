# Player class
class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        return f"{self.playerName} - {self.playerPosition}"

# NFLTeam class
class NFLTeam:
    def __init__(self, teamName, playerList):
        self.teamName = teamName
        self.playerList = playerList

    def display_team(self):
        print(f"Team Name: {self.teamName}")
        print("Players:")
        for player in self.playerList:
            print(player)

# Player Pool
player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

# Add players to a list
playerList = [player1, player2, player3, player4]

# Create team
myTeam = NFLTeam("Smashmouth Dolphins", playerList)

# Output team info
myTeam.display_team()
