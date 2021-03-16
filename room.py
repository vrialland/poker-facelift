class Room:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.observers = []
        self.finished = False

    @property
    def players_count(self):
        return len(self.players)

    @property
    def observers_count(self):
        return len(self.observers)

    def join_player(self, name):
        """
        Add a new player to the room.
        """
        player = {'name': name, 'choice': None}
        self.players.append(player)
        self.finished = False

    def join_observer(self, name):
        """
        Add a new observer to the room.
        """
        observer = {'name': name}
        self.observers.append(observer)

    def leave(self, name):
        """
        Remove a player or observer from the room.
        """
        def remove_by_name(users, name):
            for user in users:
                if user['name'] != name:
                    continue

                users.remove(user)
                return True
            return False

        if not remove_by_name(self.players, name):
            remove_by_name(self.observers, name)

    def select(self, name, choice):
        """
        Select a choice for a player.
        """
        if self.finished:
            return
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
