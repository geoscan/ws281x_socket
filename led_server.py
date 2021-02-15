import socket
import json
import board
import neopixel
from time import sleep

pixels = neopixel.NeoPixel(board.D18, 4)

def color_all(led, r,g,b):
    for i in range(0,4):
        led[i] = (r, g, b)

def color_num(led, r,g,b,n):
    if (n >= 0) and (n <= 3):
        led[n] = (r, g, b)

sleep(5)
port = 9090
print("start socket server")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', port))
print("localhost:{} bind".format(port))
server.listen(1)
color_all(pixels, 0, 0, 0)

while True:
    connection, addres = server.accept()
    data = json.loads(connection.recv(1024))
    if data['n'] == 255:
        color_all(pixels, data['r'], data['g'], data['b'])
    else:
        color_num(pixels, data['r'], data['g'], data['b'], data['n'])
    connection.close()