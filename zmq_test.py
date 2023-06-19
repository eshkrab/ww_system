import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://{SUBSCRIBER_IP}:{SUBSCRIBER_PORT}".format(
    SUBSCRIBER_IP=<SUBSCRIBER_IP>,
    SUBSCRIBER_PORT=<SUBSCRIBER_PORT>
))
topic = "state"
message = "on"
socket.send_string("%s %s" % (topic, message))
