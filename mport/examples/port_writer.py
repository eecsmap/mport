import mport
import time

port = mport.Port('port_test.dat')
flag = mport.Port('port_test.dat', offset=1)
port_count = mport.Port('port_test.dat', offset=2, port_type='<I')

STATUS_IDLE  = 0
STATUS_START = 1
STATUS_READER_READY = 2

# start reader, allow it to be ready
flag.value = STATUS_START
time.sleep(1)

print('wait for reader to be ready ...')
loop = 0
while flag.value != STATUS_READER_READY:
    loop ^= 1

start = time.time()
duration = 5 # sec
end = start + duration
count = 0
cur_value = 0
dmax = 0

while time.time() < end:
    cur_value ^= 1
    port.value = cur_value
    count += 1
    s = time.time()
    # wait feedback from reader
    while port_count.value != count:
        loop ^= 1
    # check the max delay
    d = time.time() - s
    if d > dmax: dmax = d

    #print(f'\r{count:08}\t{port.value}', end='')

# allow reader to finish
time.sleep(1)
flag.value = STATUS_IDLE

rate = count / 2 / duration

print(f'\nrate: {rate}Hz\tcount: {count}\tmax delay: {dmax}\tSafe frequence:{1/dmax}')
