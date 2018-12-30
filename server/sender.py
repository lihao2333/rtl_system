from SocketBox.socketSP import socketPub
import time
HOST = "0.0.0.0"
PORT = 50000
with socketPub(HOST, PORT) as pub:
    while True :
        pub.publish(b"123")
        print("123")
        time.sleep(1)

