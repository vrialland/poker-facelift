from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

app.debug = True

@socketio.on('join')
def handle_join(name):
    print(f'New user joined {name}')


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    socketio.run(app)
