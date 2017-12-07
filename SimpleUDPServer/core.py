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
PROTOCOL_ACK = '#$000001$FF$FF$#'
PROTOCOL_NAK = '#$$#'

try:
    # create UDP socket
    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # reuse socket if in wait_state
    udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind it to address
    udpSocket.bind((HOST,PORT))
except socket.error, msg:
    print "Failed to create and bind socket." +\
        "Error code: " + str(msg[0]) +\
        "Error message: " + msg[1]
    sys.exit()

# Main Server Loop
while 1:
    udpPacket = udpSocket.recvfrom(1024)
    receivedData = udpPacket[0]
    receivedAddr = udpPacket[1]

    # process data
    # strip data of strange characters
    receivedData = receivedData.rstrip()

    # check if valid message is received
    if receivedData.startswith('#$') and receivedData.endswith('$#'):
        # valid data, begin processing
        try:
            # split data into parts
            splitData = receivedData[2:-2].split('$')
            protocolVersion = split_data[0]
            protocolCommand = split_data[1]
            protocolParams = split_data[2:-2]
            protocolChkSum = split_data[-1:]

            # test simple command, later to be rewritten
            if protocolCommand == '00':
                reply = '#$000001$FF$PiMediaServer$RDY$00$#'
            elif protocolCommand == '01':
                reply = '#$000001$FF$01$01$#'
            else:
                reply = PROTOCOL_ACK
        except:
            reply = PROTOCOL_NAK
    else:
        reply = PROTOCOL_NAK + '@' + receivedData + ' from ' +\
            receivedAddr[0] + ':' + str(receivedAddr[1]) + '\n'

    udpSocket.sendto(reply,receivedAddr)
    print("Send "+reply+" to "+receivedAddr[0]+":"+str(receivedAddr[1])+"\n")


# Exit server
udpSocket.close()
