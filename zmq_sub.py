import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://*:5555")
socket.setsockopt(zmq.SUBSCRIBE, b"brightness")

topic = b'brightness\0'
message = "100"

print( await socket.recv_multipart())

