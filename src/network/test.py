'''
Created on 1 avr. 2014

@author: egor
'''

import socket

if __name__ == '__main__':
    HOST = 'localhost'    # The remote host
    PORT = 9999              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    s.close()
    print('Received', repr(data))