# This is a simple networked application that can both send and
# receive data. Think of it as "telnet".

import logging

assignedport = {}

class SimpleApp:
    def __init__(self, port, layer4):
        # Save the layer 4 object as a instance variable so we can reference it later
        self.layer4 = layer4
        # Open a new socket to listen on, passing the callback functions for receiving a message and the port
        self.layer4.connect_to_socket(self.receive, port)

    def receive(self, data):
        print(f"Client received message: {data}")

    def send(self, receiver_addr, send_port, recv_port, data):
        # Send a message to a receiver, passing the right port
        self.layer4.from_layer_5(data, send_port, recv_port, receiver_addr)
