# module to get appropriate RGBW values for any given time of day.


def linappr(x,x1,x2,y1,y2):
    """ solves the equation y = kx + m  and returns the actual value for x"""
    k = (y2-y1)/(x2-x1)
    m = y1-k*x1
    y = k*x+m
    return int(y)






def get_rgbw(timecurrent,maxval):
    # insert actual time and maximum value for RGBW value PWM signal
    # output is a list of RGBW values

    # Old value matrix
    r =        [0, 2, 30, 30,   80, 500, 200,   100,  5,    1,  0]
    g =        [0, 0, 0,   0,   0,  100,  0,    0,    0,    0,  0]
    b =        [0, 10,80, 120,  200, 800, 1000, 400 , 20,   5,  0]
    w =        [0, 2, 30, 60,   400, 80,  100,  30,   2,    1,  0]
    timeline = [0, 6, 7.3, 8.0,  11,  13,  20,  20.8, 21.5, 22, 23.5]


    # new value matrix
    r =        [0, 0,   2,  30,  30,  100,  100,   500,   100,   5,    1,   0,    0]
    g =        [0, 0,   0,  0,   0,   0,    0,     0,     0,     0,    0,   0,    0]
    b =        [0, 0,   10, 80,  120, 1000, 1000,  1000,  400 ,  20,   10,  0,    0]
    w =        [0, 0,   2,  30,  60,  200,  200,   100,   30,    2,    2,   0,    0]
    timeline = [0, 5.9, 6,  7.3, 9.0, 11,   13,     20,   20.8,  21.5, 22,  23.5, 24]






    # some "good" values
    # values to range from 0 - 1024 for Adafruit Huzzah feather PWM
    # =================================
    # 20:0:30:100 - nice weak "daylight" to see the fishes
    # 100:0:1024:100 - strong blueish
    # =================================



    # find the index for the current time
    timeindex = -1

    # for x in range(0, 3):
    for t in timeline:
        if timecurrent <= t:
            break
        else:
            timeindex += 1
    # print(timeindex)

    rOut = linappr(timecurrent,timeline[timeindex],timeline[timeindex+1],r[timeindex],r[timeindex+1] )
    gOut = linappr(timecurrent,timeline[timeindex],timeline[timeindex+1],g[timeindex],g[timeindex+1] )
    bOut = linappr(timecurrent,timeline[timeindex],timeline[timeindex+1],b[timeindex],b[timeindex+1] )
    wOut = linappr(timecurrent,timeline[timeindex],timeline[timeindex+1],w[timeindex],w[timeindex+1] )

    # out = [r[timeindex], g[timeindex], b[timeindex], w[timeindex]]
    # out = [0,0,0,0]
    out = [rOut,gOut,bOut,wOut]

    return out

# main program starts here!
"""
print('-------------')
print(i)
print(time[i]
print(get_rgbw(5.3,1023))"""
