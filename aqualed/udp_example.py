import socket
import sys
import time

import rgbwtranslation

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print ('Failed to create socket')
    sys.exit()

host = '192.168.0.118'
# host = 'localhost'
port = 8888
timestart = time.time()
current_time = 0

while 1 :
    time.sleep(1)
    try :
        # msg = input('Enter message to send : ')
        msg = '1:1:2:255'
        # print(msg)
        # print(time.time()-timestart)
        current_time = time.time() - timestart
        rgbw = rgbwtranslation.get_rgbw(current_time,1024)
        outstr = str(rgbw[0]) + ':' + str(rgbw[1]) + ':' + str(rgbw[2]) + ':' + str(rgbw[3])
        print('RGBW: ' + outstr)

        #Set the whole string
        s.sendto(outstr.encode('utf-8'), (host, port))
    # Some problem sending data ??
    except socket.error as e:
        print ('Error Code : ' + str(e[0]) + ' Message ' + e[1])
        sys.exit()



print('Program Complete')
