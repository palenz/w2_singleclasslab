class Team:

    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player):
        return player in self.players

    def play_game(self, won_game):
        if won_game == True:
            self.points += 3