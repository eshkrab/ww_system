import zmq
import time
import sys

port = sys.argv[1] if len(sys.argv) > 1 else "5555"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(f"tcp://*:{port}")

topic = "brightness"
message = "100"

while True:
    socket.send_string(topic + message)
    print(f"{topic} {message}")
    time.sleep(0.1)

