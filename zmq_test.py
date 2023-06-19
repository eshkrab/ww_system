import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")
topic = b'brightness\0'
message = "100"
socket.send_multipart( [topic, message] )
print("%s %s" % (topic, message)
