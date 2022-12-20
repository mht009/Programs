from machine import I2C, Pin
from math import sqrt, atan2, pi, copysign, sin, cos
from mpu9250 import MPU9250
from time import sleep
import sys


# addresses 
MPU = 0x68
id = 0
sda = Pin(0)
scl = Pin(1)

# create the I2C
i2c = I2C(id=id, scl=scl, sda=sda)

# Scan the bus
print(i2c.scan())
mht = MPU9250(i2c)

print("ax = ", mht.gyro([0]))

try:
    while True:
        # print("ax = ", mht.acceleration([0]))

        accel = mpu9250.acceleration([0])
        print(" ax = " , ( accel ))
        print(" ay = " , ( accel[1] ))
        print(" az = " , ( accel[2] ))

        gyro = mpu9250.readGyro()
        print(" gx = " , ( gyro['x'] ))
        print(" gy = " , ( gyro['y'] ))
        print(" gz = " , ( gyro['z'] ))

        mag = mpu9250.readMagnet()
        print(" mx = " , ( mag['x'] ))
        print(" my = " , ( mag['y'] ))
        print(" mz = " , ( mag['z'] ))
        print()

        time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit(0)