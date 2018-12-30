import sys
import zmq

port = "5556"

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect ("tcp://127.0.0.1:%s" % port)

# Subscribe to zipcode, default is NYC, 10001
topicfilter = "10001"
topicfilter = ""
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

# Process 5 updates
total_value = 0
for update_nbr in range (50000):
    string = socket.recv()
    print(string)

      
