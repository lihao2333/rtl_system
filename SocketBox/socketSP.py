"as a subsriber  using zeromq"
import time
import zmq
import sys
class socketPub():
    def __init__(self, host, port): 
        self.host = host
        self.port = port
        self.context = zmq.Context()
    def __enter__(self):
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind("tcp://%s:%d"%(self.host, self.port))
        time.sleep(0.2)#再bind和send之间必须有一段延时, 否则可能会遗漏发送!!!!
        return self
    def __exit__(self, type, value, traceback):
        pass
        self.socket.close()
    def publish(self,element, type="pyobj"):  
        if type == "pyobj":
            self.socket.send_pyobj(element)
        if type == "bytes":
            self.socket.send(element)
class socketSub():
    def __init__(self, targets):#targets means[(host1, port1), (host2, port2)], for multi-publish
        self.context = zmq.Context()
        self.targets = targets
        self.sockets = []
    def __enter__(self):
        for host, port in self.targets:
            socket = self.context.socket(zmq.SUB)
            socket.connect("tcp://%s:%d"%(host, port))
            socket.setsockopt(zmq.SUBSCRIBE, b"")# 设置过滤选项, 此处不设置
            self.sockets.append(socket)
        return self
    def __exit__(self, type, value, traceback):
        for socket in self.sockets:
            socket.close()

    def subscribe(self,type="pyobj",times=sys.maxsize):
        for i in range(times):
            res = []
            for socket in self.sockets:
                if type == "pyobj":
                    element = socket.recv_pyobj()
                if type == "bytes":
                    element = socket.recv()
                res.append(element)
            yield res
