from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

app.debug = True

participants = []

@socketio.on('join')
def handle_join(name):
    participants.append(name)
    emit('participants_update', participants, broadcast=True)


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    socketio.run(app)
