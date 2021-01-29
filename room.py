class Room:
    def __init__(self):
        self.players = []
        self.finished = False

    def join(self, name):
        """
        Add a player to the player list.
        """
        player = {'name': name, 'choice': None}
        self.players.append(player)
        self.finished = False

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
        finished = True
        for player in self.players:
            if player['name'] == name:
                player['choice'] = choice
            else:
                finished = finished and (player['choice'])
        self.finished = finished

    def clear(self):
        """
        Clear players votes
        """
        for player in self.players:
            player['choice'] = None
        self.finished = False

    def reveal(self):
        """
        Force the end of voting session
        """
        self.finished = True
