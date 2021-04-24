# mport
IO port based on shared memory map (mmap).

## install
```
pip install mport
```

## Usage
* Prototype protocols
* Build control layer and/or data collection layer for AI training applications
* Broadcast operations to multiple receiving applications
* Hardware simulation where you have virtual devices running as separate processes yet communicate via ports

Example Reader
```
import mport

speed_port = mport.Port('io.dat')
light_port = mport.Port('io.dat', offset=2)

while True:
  car.set_speed(speed_port.value)
  car.light(light_port.value)
```

Example speed controller
```
import mport

speed_port = mport.Port('io.dat')

speed_port.value = 42
```

Example light controller
```
import mport

light_port = mport.Port('io.dat', offset=2)
light_port.value = True
```
