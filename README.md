# Real-Time Chat Application

## Overview

This project is a simple real-time chat application built using Flask and Socket.IO. It allows multiple users to communicate instantly through a web interface. The app provides a smooth chatting experience with features like usernames, timestamps, and a clean WhatsApp-like UI.

## Features

* Real-time messaging using WebSockets
* Multiple users can chat simultaneously
* Username-based communication
* Left/right message alignment
* Timestamp for each message
* Send messages using Enter key
* Clean and responsive user interface

## Technologies Used

* Frontend: HTML, CSS, JavaScript
* Backend: Python (Flask)
* Real-time: Flask-SocketIO (WebSockets)
* Server: Gunicorn + Eventlet
* Version Control: Git & GitHub

## Working

Users open the application in a browser and enter their username. When a message is sent, it is transmitted to the server using WebSockets. The server processes the message and broadcasts it to all connected users in real time. This ensures instant message delivery without refreshing the page.

## Run Locally

Install dependencies and start the server:

```bash
pip install flask flask-socketio
python app.py
```

Then open: http://127.0.0.1:5000

## Conclusion

This project demonstrates the use of WebSockets for real-time communication. It is beginner-friendly and helps understand how modern chat applications work, making it suitable for academic projects and learning purposes.

