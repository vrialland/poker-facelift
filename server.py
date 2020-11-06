from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

app.debug = True

participants = []


class Room:
    def __init__(self):
        self.players = []

    def join(self, name):
        player = {'name': name, 'choice': None}
        self.players.append(player)
        self.broadcast_players()

    def leave(self, name):
        for player in self.players:
            if player['name'] == name:
                self.players.remove(player)
                self.broadcast_players()
                break

    def select(self, name, choice):
        for player in self.players:
            if player['name'] == name:
                player['choice'] = choice
                self.broadcast_players()
                break

    def broadcast_players(self):
        emit('players_update', self.players, broadcast=True)


room = Room()


@socketio.on('join')
def handle_join(name):
    room.join(name)


@socketio.on('left')
def handle_left(name):
    room.leave(name)


@socketio.on('select')
def handle_select(player):
    room.select(player['name'], player['choice'])




@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    socketio.run(app)
