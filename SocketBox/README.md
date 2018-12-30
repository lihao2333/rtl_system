## interface for zeroMQ in SUB/PUB mod
.
|---socketSP.py    --define class of subscribe and publish
|---testSP.py        --unittest for socketSP.py
|---test.sh        --run unittest
## test
* `bash test.sh`
## usage
```python
#publish
from socketSP import socketPub
    with socketPub("127.0.0.1", 5556) as pub:
        pub.publish("hihi")
```
```python
#subsribe
from socketSP import socketSub
    with socketSub("127.0.0.1", 5556) as sub:
        for string in sub.subscribe(10): ## receive 10 frame. default value is  sys.maxsize
            print(string)
```
            
