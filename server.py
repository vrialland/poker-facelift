from flask import Flask
from flask_socketio import SocketIO, emit

from room import Room

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

app.debug = True

participants = []


room = Room()


def broadcast_room(room):
    emit(
        'room_update',
        {
            'players': room.players,
            'finished': room.finished
        },
        broadcast=True)


@socketio.on('join')
def handle_join(name):
    room.join(name)
    broadcast_room(room)


@socketio.on('left')
def handle_left(name):
    room.leave(name)
    broadcast_room(room)


@socketio.on('select')
def handle_select(player):
    room.select(player['name'], player['choice'])
    broadcast_room(room)


@socketio.on('clear')
def handle_clear():
    room.clear()
    broadcast_room(room)


@socketio.on('reveal')
def handle_reveal():
    room.reveal()
    broadcast_room(room)


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    socketio.run(app)
