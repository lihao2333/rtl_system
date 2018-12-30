'为了测试阻塞'
import socketIPC
import time
address = "/tmp/test-socket"
with socketIPC.socketIpcPub(address) as pub:
    for i in range(10000000):
        print(i)
        pub.publish({1,2,3}, type="pyobj")
        time.sleep(0.5)
