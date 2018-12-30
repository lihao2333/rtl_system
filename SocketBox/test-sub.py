from socketSP import socketSub
import time
import sys
sys.path.append("..")
from config_emulate import (
        host_decision_trafficLight, 
        host_decision_trajectory, 
        port_decision_trafficLight, 
        port_decision_trajectory
        )
host_decision_trajectory = "127.0.0.1"
host_decision_trafficLight = "127.0.0.1"
from myProtobuf import traffic_light_pb2, trajectory_pb2
from myProtobuf.traffic_light_pb2 import TrafficInfo
from myProtobuf.trajectory_pb2 import TrajectoryInfo
def sub_all():
    with socketSub([
        (host_decision_trajectory, portcv_decision_trajectory), 
        (host_decision_trafficLight, port_decision_trafficLight)
        ]) as sub:
        x = time.time()
        with open("output", "wb") as fout:
            for rxs in sub.subscribe():
                print(time.time() - x)
                trajectory = TrajectoryInfo()
                trajectory.ParseFromString(rxs[0])
                print(len(rxs[0]), len(rxs[1]))
                trafficLight = TrafficInfo()
                trafficLight.ParseFromString(rxs[1])
                print(trafficLight)
                x  = time.time()
def sub_trajecotry():
    with socketSub([
        (host_decision_trajectory, port_decision_trajectory), 
        ]) as sub:
        x = time.time()
        with open("output", "wb") as fout:
            for rxs in sub.subscribe():
                print(time.time() - x)
                trajectory = TrajectoryInfo()
                trajectory.ParseFromString(rxs[0])
                print(trajectory)
                x  = time.time()
def sub_trafficLight():
    with socketSub([
        (host_decision_trafficLight, port_decision_trafficLight)
        ]) as sub:
        x = time.time()
        with open("output", "wb") as fout:
            for rxs in sub.subscribe():
                print(time.time() - x)
                print(rxs[0])
                trafficLight = TrafficInfo()
                trafficLight.ParseFromString(rxs[0])
                print(trafficLight)
                x  = time.time()
sub_trafficLight()
#sub_trajecotry()
#sub_all()
