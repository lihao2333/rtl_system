from SocketBox.socketSP import socketPub
import datetime
import time
HOST = "0.0.0.0"
PORT = 50000
DELAY_SECOND = 5
def get_test_time(delay_second):
    now = datetime.datetime.now()
    return "%02d%02d%02d"%(now.hour, now.minute, now.second+delay_second)
TO_SEND = {
        "time":get_test_time(DELAY_SECOND),
        "params":{
            "sample_rate":2.048e6 ,
            "center_freq":70e6    ,
            "freq_correction":60  ,
            "gain":'auto',
            "sample_num":512
            }
        }
with socketPub(HOST, PORT) as pub:
    pub.publish(TO_SEND, type="pyobj")

