from flask import Flask, render_template
from flask_socketio import SocketIO, send
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# store messages
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

# receive message
@socketio.on('message')
def handle_message(data):
    data['time'] = datetime.now().strftime("%I:%M %p")  # time
    messages.append(data)
    send(data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)