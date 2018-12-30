from SocketBox.socketSP import socketPub
import time
HOST = "0.0.0.0"
PORT = 50000
TO_SEND = {
        "time":"163000"
        }
with socketPub(HOST, PORT) as pub:
    pub.publish(TO_SEND, type="pyobj")

