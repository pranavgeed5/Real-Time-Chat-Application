import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO, send
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@socketio.on('message')
def handle_message(data):
    data['time'] = datetime.now().strftime("%I:%M %p")
    messages.append(data)
    send(data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)