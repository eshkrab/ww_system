import zmq
import time
import sys

if len(sys.argv) < 2:
    print("Please provide a port number as a command-line argument.")
    sys.exit(1)

port = sys.argv[1]
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://localhost:{port}")
socket.setsockopt_string(zmq.SUBSCRIBE, "")

print("I am ready to receive")

topic = b'brightness\0'
message = "100"

while True:
    received_message = socket.recv_string()
    print(received_message)

    # Modulate the value based on time
    current_time = time.time()
    value = int(current_time % 60)  # Modulate between 0 and 59
    message = str(value)

    # Perform any necessary processing or actions based on the received message
    # ...

    time.sleep(0.1)

