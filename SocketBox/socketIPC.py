"as a subsriber  using zeromq"
import time
import zmq
import sys
class socketIpcPub():
    def __init__(self,address ): 
        self.address = address
        self.context = zmq.Context()
    def __enter__(self):
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind("ipc://%s"%(self.address))
        time.sleep(0.2)#再bind和send之间必须有一段延时, 否则可能会遗漏发送!!!!
        return self
    def __exit__(self, type, value, traceback):
        pass
        self.socket.close()
    def publish(self,element, type = "bytes"):  
        if type == "bytes":
            self.socket.send(element)
        if type == "pyobj":
            self.socket.send_pyobj(element)
class socketIpcSub():
    def __init__(self, targets, drop = False, timeout=-1):#targets means[(host1, port1), (host2, port2)], for multi-publish
        self.context = zmq.Context()
        self.targets = targets
        self.timeout = timeout
        self.sockets = []
        self.drop = drop
    def __enter__(self):
        for address in self.targets:
            socket = self.context.socket(zmq.SUB)
            if self.drop:
                socket.setsockopt(zmq.CONFLATE, 1)
            socket.connect("ipc://%s"%(address))
            socket.setsockopt(zmq.SUBSCRIBE, b"")# 设置过滤选项, 此处不设置
            socket.setsockopt(zmq.RCVTIMEO,self.timeout)
            self.sockets.append(socket)
        return self
    def __exit__(self, type, value, traceback):
        for socket in self.sockets:
            socket.close()
    def subscribe(self,type="bytes", times=sys.maxsize):
        for i in range(times):
            res = []
            for socket in self.sockets:
                if type == "bytes":
                    element = socket.recv()
                elif type == "pyobj":
                    element = socket.recv_pyobj()
                res.append(element)
            yield res


