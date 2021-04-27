import mport
import time

port = mport.Port('port_test.dat')
flag = mport.Port('port_test.dat', offset=1)
port_count = mport.Port('port_test.dat', offset=2, port_type='<I')

STATUS_IDLE  = 0
STATUS_START = 1
STATUS_READY = 2

count = 0
total = 0
prev_value = 0

loop = 0
while flag.value == STATUS_IDLE:
    loop ^= 1

flag.value = STATUS_READY

while flag.value:
    cur_value = port.value
    if cur_value ^ prev_value:
        prev_value = cur_value
        count += 1
        port_count.value = count
    total += 1

print(f'\ncount: {count}\ttotal: {total}')
