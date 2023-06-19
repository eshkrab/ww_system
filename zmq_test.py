import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")
topic = "brightness"
message = "100"
socket.send_string("%s %s" % (topic, message))
