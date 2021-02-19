from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, emit

from room import Room

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


participants = []


room = Room()


def broadcast_room(room):
    emit(
        'room_update',
        {
            'players': room.players,
            'observers': room.observers,
            'finished': room.finished
        },
        broadcast=True)


@socketio.on('join_player')
def handle_join_player(name):
    room.join_player(name)
    broadcast_room(room)


@socketio.on('join_observer')
def handle_join_observer(name):
    room.join_observer(name)
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
    return render_template('index.jinja', env=app.config['ENV'])


if __name__ == '__main__':
    socketio.run(app)
