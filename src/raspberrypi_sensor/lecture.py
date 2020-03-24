import serial
import time
import socket
import sys

hote = ''
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print ("Connexion en cours sur le port local {}".format(port))

ser = serial.Serial('/dev/ttyACM1', 9600)
while True:
        try:
            message = ser.readline()
            print (sys.stderr, 'sending "%s"' % message)
            socket.sendall(message)
            raise SerialException('read failed: {}'.format(e))
        except serial.serialutil.SerialException as exception:
            a=1
        

