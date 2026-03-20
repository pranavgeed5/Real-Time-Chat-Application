from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# ✅ IMPORTANT FIX
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    timestamp = datetime.now().strftime('%H:%M')

    # ✅ USE emit instead of send
    emit('message', {
        'msg': data['msg'],
        'user': data['user'],
        'time': timestamp
    }, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=10000)