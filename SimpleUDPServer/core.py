#!/usr/bin/python

"""
Simple UDP Server

"""

# import part
import socket
import sys

# Global defines
HOST = ''       # Symbolic name meaning all available interfaces
PORT = 12345    # Arbitrary no-privileged port used for the server

try:
    # create UDP socket
    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSocket.bind((HOST,PORT))
except socket.error, msg:
    print "Failed to create and bind socket." +
    / "Error code: " + str(msg[0]) +
    / "Error message: " + msg[1]
    sys.exit()

# Main Server Loop
while 1:
    udpPacket = udpSocket.recvfrom(1024)
    recivedData = udpPacket[0]
    recivedAddr = udpPacket[1]

# Exit server
udpSocket.close()
