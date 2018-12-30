from socketSP import socketPub
host="127.0.0.1"
port=5556
with socketPub(host, port) as pub:
    while True:
        pub.publish(b"hihihi")
