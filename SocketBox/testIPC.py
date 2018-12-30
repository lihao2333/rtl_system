import unittest
import time
from socketIPC import socketIpcPub, socketIpcSub
from multiprocessing import Process, Queue
host = "127.0.0.1"
address="/tmp/testSocket"
address2="/tmp/testSocket2"
class TestSocketPub(unittest.TestCase):
    def test_publish(self):
        with socketIpcPub(address) as pub:
            pub.publish(b"123")
class TestSocketSub(unittest.TestCase):
    def test1_subscribe(self):
        CNT = 100
        def publish(q_pub):
            with socketIpcPub(address) as pub:
                for i in range(CNT):
                    pub.publish(str(i).encode())
                    q_pub.put(str(i).encode())
            time.sleep(1)
        def subscribe(q_sub):
            with socketIpcSub([address]) as sub:
                for string in sub.subscribe(CNT):
                    q_sub.put(string[0])
        q_pub, q_sub = Queue(), Queue() 
        p_pub = Process(target=publish, args=(q_pub, ))
        p_sub = Process(target=subscribe, args=(q_sub, ))
        p_sub.start()
        p_pub.start()
        p_sub.join()
        for i in range(CNT):
            self.assertEqual(q_pub.get(), q_sub.get())
    def test_1sub2pub(self):
        CNT = 10
        def publish(q_pub):
            with socketIpcPub(address) as pub:
                with socketIpcPub(address2) as pub2:
                    for i in range(CNT):
                        pub.publish(str(i).encode())
                        print("publish", i)
                        q_pub.put(str(i).encode())
                        pub2.publish(str(i).encode())
                        print("publish2", i)
                        q_pub.put(str(i).encode())
        def subscribe(q_sub):
            with socketIpcSub([address, address2]) as sub:
                for string  in sub.subscribe(CNT):
                    print("receive",string)
                    for ele in string:
                        q_sub.put(ele)
        q_pub, q_sub = Queue(), Queue() 
        p_pub = Process(target=publish, args=(q_pub, ))
        p_sub = Process(target=subscribe, args=(q_sub, ))
        p_sub.start()
        p_pub.start()
        p_sub.join()
        for i in range(CNT):
            pub = q_pub.get()
            sub = q_sub.get()
            print(type(pub),type(sub))
            self.assertEqual(q_pub.get(), q_sub.get())

            
        
#if __name__ == "__main__":
#    with socketIpcPub(host, port) as pub:
#        pub.publish("123")
