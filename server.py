from flask import Flask
from flask_socketio import SocketIO, emit

from room import Room

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

app.debug = True

participants = []


room = Room()


def broadcast_players(room):
    emit('players_update', room.players, broadcast=True)


@socketio.on('join')
def handle_join(name):
    room.join(name)
    broadcast_players(room)


@socketio.on('left')
def handle_left(name):
    room.leave(name)
    broadcast_players(room)


@socketio.on('select')
def handle_select(player):
    room.select(player['name'], player['choice'])
    broadcast_players(room)


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    socketio.run(app)
