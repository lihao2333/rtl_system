import socket
import json
from multiprocessing import Process, Pool
import time
class SocketTCP():
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def sendString(self,string):
        sk = socket.socket()
        sk.connect((self.host,self.port))
        sk.sendall(string.encode("utf-8"))
        sk.close()
    def sendBigString(self, string):
        bytes_ = string.encode("utf-8")
        length = len(bytes_)
        self.sendString(json.dumps({"length":length}))
        self.sendString(string)
    def receiveBigString(self, tap=4096):
        sk = socket.socket()
        sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sk.bind((self.host, self.port))
        sk.listen(5)
        while True:
            conn, addr = sk.accept()
            data = conn.recv(1024).decode("utf-8")
            remain = json.loads(data)["length"]
            conn.close()
            conn, addr = sk.accept()
            temp = 0
            data = b''
            while remain>0:
                toRead = tap if remain>tap else remain
                data += conn.recv(toRead)
                temp += toRead
                remain -= toRead
            conn.close()
            string = data.decode("utf-8")
            yield string
def  testSend():
    while True:
        for i in range(1000):
            print("sending", i)
            SocketTCP(host, port).sendBigString(str(i))
            time.sleep(0.001)
            print("hi")
def testReceive():
    print("start receiving")
    for string in SocketTCP(host, port).receiveBigString():
        print("received", string)
def test2Single():
    testReceive()
def test():
    print("test start")
    p = Pool(5)
    p.apply_async(testSend, ())
    p.apply_async(testReceive, ())
    p.close()
    p.join()
    print("test end")
    time.sleep(10)
#test()
if __name__=="__main__":
    test()
#    testSend()
#test2Single()


