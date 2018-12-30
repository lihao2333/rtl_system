from SocketBox.socketSP import socketPub, socketSub
from gps.gps import wait_time
from sdr.MySdr import MySdr
SERVER_HOST = "10.112.254.131"
SERVER_PORT = 50000
with socketSub([(SERVER_HOST, SERVER_PORT)]) as sub:
    my_sdr = MySdr()
    for recvs in sub.subscribe(type="pyobj"):
        print("recv:",recvs[0])
        my_sdr.set_paras(recvs[0]["params"])
        wait_time(recvs[0]["time"])
        data = my_sdr.sample_data()
        print(data)

