import socketIPC
import time
address = "/tmp/test-socket"
with socketIPC.socketIpcSub([address]) as sub:
    while True:
        for no, recv in enumerate(sub.subscribe(type="pyobj") ):
            print(recv[0])
            time.sleep(1)
