'''This file will hold all the helper functions that are required for the Air Quality app.'''
import socket

def local_ip():
    '''Will attempt to get the computer's IP on the local internet.'''
    socket_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_connection.connect(("8.8.8.8", 80))
    return socket_connection.getsockname()[0]
