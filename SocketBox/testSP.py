import unittest
import time
from socketSP import socketPub, socketSub
from multiprocessing import Process, Queue
host = "127.0.0.1"
port = 5556
port2 = 5557
class TestSocketPub(unittest.TestCase):
    def test_publish(self):
        with socketPub(host, port) as pub:
            pub.publish(b"123")
class TestSocketSub(unittest.TestCase):
    def test1_subscribe(self):
        CNT = 100
        def publish(q_pub):
            with socketPub(host, port) as pub:
                for i in range(CNT):
                    pub.publish(str(i).encode())
                    q_pub.put(str(i).encode())
            time.sleep(1)
        def subscribe(q_sub):
            with socketSub([(host, port)]) as sub:
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
            with socketPub(host, port) as pub:
                with socketPub(host, port2) as pub2:
                    for i in range(CNT):
                        pub.publish(str(i).encode())
                        print("publish", i)
                        q_pub.put(str(i).encode())
                        pub2.publish(str(i).encode())
                        print("publish2", i)
                        q_pub.put(str(i).encode())
        def subscribe(q_sub):
            with socketSub([(host, port),(host, port2)]) as sub:
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
            self.assertEqual(q_pub.get(), q_sub.get())

            
        
#if __name__ == "__main__":
#    with socketPub(host, port) as pub:
#        pub.publish("123")
