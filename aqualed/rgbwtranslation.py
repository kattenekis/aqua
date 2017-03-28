# module to get appropriate RGBW values for any given time of day.

def get_rgbw(timecurrent,maxval):
    # insert actual time and maximum value for RGBW value PWM signal
    # output is a list of RGBW values

    r =        [0, 2, 30, 30,   80, 500, 200,   100,  5,    1,  0]
    g =        [0, 0, 0,   0,   0,  100,  0,    0,    0,    0,  0]
    b =        [0, 10,80, 120,  200, 800, 1000, 400 , 20,   5,  0]
    w =        [0, 2, 30, 60,   400, 80,  100,  30,   2,    1,  0]
    timeline = [0, 6, 7.3, 8.0,  11,  13,  20,  20.8, 21.5, 22, 23.5]

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
    out = [r[timeindex], g[timeindex], b[timeindex], w[timeindex]]
    # out = [0,0,0,0]
    return out

# main program starts here!
"""
print('-------------')
print(i)
print(time[i]
print(get_rgbw(5.3,1023))"""
