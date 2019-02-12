#!/usr/bin/env python3

import configparser
import socket
import sys
import time
import datetime
import rgbwtranslation

# read configurationfile config.ini
config = configparser.ConfigParser()
config.read('aqualed.ini')
host = config['DEFAULT']['aqualed_client_ip']
port = int(config['DEFAULT']['aqualed_client_port'])
looptime = float(config['DEFAULT']['looptime'])

print('client IP:   ', host)
print('client port: ', port)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print ('Failed to create socket')
    sys.exit()


timestart = time.time()
current_time = 0

while 1 :
    time.sleep(looptime)

    # code to fake time - debugging
    """
    current_time += 0.1
    if current_time >=24:
        current_time = 0
    """
    # code for real time use:
    now =  datetime.datetime.now()
    current_time = float(now.hour)+float(now.minute)/60

    print('Time of day: {:.2f} [hour]'.format(current_time), end=" ")
    try :
        rgbw = rgbwtranslation.get_rgbw(current_time,1024)
        outstr = str(rgbw[0]) + ':' + str(rgbw[1]) + ':' + str(rgbw[2]) + ':' + str(rgbw[3])
        print('   RGBW string: ' + outstr)
        #Send the whole string
        s.sendto(outstr.encode('utf-8'), (host, port))
    # Some problem sending data ??
    except socket.error as e:
        print ('Error Code : ' + str(e[0]) + ' Message ' + e[1])
        sys.exit()

print('Program Complete')
