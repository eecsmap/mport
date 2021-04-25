import mport
import random
import time

rgb = mport.Port('rgb.dat', port_type='<I')

while True:
    rgb.value = random.randint(0, 0x00ffffff)
    time.sleep(1)
