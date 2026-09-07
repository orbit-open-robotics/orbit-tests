from orbit.pan_tilt import PanTilt
from time import sleep

pan = PanTilt()
pan.initialize()

print('home')
pan.home(time = 1)
sleep(1)

print('tilt up')
pan.tilt_up(time = 1)
sleep(1)

print('tilt down')
pan.tilt_down(time = 1)
sleep(1)

print('home')
pan.home(time = 1)
sleep(1)

print('pan left')
pan.pan_left(time = 1)
sleep(1)

print('home')
pan.home(time = 1)
sleep(1)

print('pan right')
pan.pan_right(time = 1)
sleep(1)

print('home')
pan.home(time = 1)
sleep(1)

pan.off()