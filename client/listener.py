from SocketBox.socketSP import socketPub, socketSub
from gps.gps import wait_time
SERVER_HOST = "10.112.254.131"
SERVER_PORT = 50000
with socketSub([(SERVER_HOST, SERVER_PORT)]) as sub:
    for recvs in sub.subscribe(type="pyobj"):
        print("recv:",recvs[0])
        wait_time(recvs[0]["time"])
