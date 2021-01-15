class Room:
    def __init__(self):
        self.players = []

    def join(self, name):
        """
        Add a player to the player list.
        """
        player = {'name': name, 'choice': None}
        self.players.append(player)

    def leave(self, name):
        """
        Remove a player from the player list.
        """
        for player in self.players:
            if player['name'] != name:
                continue

            self.players.remove(player)
            return

    def select(self, name, choice):
        """
        Select a choice for a player.
        """
        for player in self.players:
            if player['name'] != name:
                continue

            player['choice'] = choice
            return

    def clear(self):
        """
        Clear players votes
        """
        for player in self.players:
            player['choice'] = None
