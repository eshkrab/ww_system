import zmq
import zmq.asyncio
import asyncio
import time
import sys

async def main():
    if len(sys.argv) < 2:
        print("Please provide a port number as a command-line argument.")
        sys.exit(1)

    port = sys.argv[1]
    context = zmq.asyncio.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(f"tcp://localhost:{port}")
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    print("I am ready to receive")


    while True:
        received_message = await socket.recv_string()
        print(received_message)


        await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())

