import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")
topic = "brightness"
message = "100"
while True:
    socket.send_string(  topic + message )
    print("%s %s" % (topic, message))
    time.sleep(1)
