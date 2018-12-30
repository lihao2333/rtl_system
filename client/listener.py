from SocketBox.socketSP import socketPub, socketSub
from gps.gps import wait_time
from sdr.MySdr import MySdr
import zmq
PORT = '50000'
context =  zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s"%PORT)
my_sdr = MySdr()
while True:
    recv = socket.recv_pyobj()
    print("recv:",recv)
    my_sdr.set_paras(recv["params"])
    wait_time(recv["time"])
    data = my_sdr.sample_data()
    socket.send_pyobj(data)
    print(data)

