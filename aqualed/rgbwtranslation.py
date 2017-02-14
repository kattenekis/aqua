
"""
r =    [2,2,100,225,225,225,225,255,2,2]
g =    [0,0,0,104,220,220,150,100,0,0]
b =    [7,10,200,0,100,100,0,0,7,7]
w =    [2,2,100,200,255,255,180,60,2,2]
time = [0,3.6,5.4,7.2,11,20,20.5,20.8,21.6,24]

timestop = 44.0
i = -1
for t in time:
    print(r[i], ',', g[i], ',', b[i], ',', w[i])
    if t>=timestop:
        # print('hurray!')
        # print(r[i], ',', g[i], ',', b[i], ',', w[i])
        break
    i += 1
"""

def get_rgbw(timecurrent,maxval):
    # insert actual time and maximum value for RGBW value PWM signal
    # output is a list of RGBW values

    r = [2, 2, 100, 225, 225, 225, 225, 255, 2, 2]
    g = [0, 0, 0, 104, 220, 220, 150, 100, 0, 0]
    b = [7, 10, 200, 0, 100, 100, 0, 0, 7, 7]
    w = [2, 2, 100, 200, 255, 255, 180, 60, 2, 2]
    timeline = [0, 3.6, 5.4, 7.2, 11, 20, 20.5, 20.8, 21.6, 24]

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

print('-------------')
"""print(i)
print(time[i])"""
print(get_rgbw(5.3,1023))
