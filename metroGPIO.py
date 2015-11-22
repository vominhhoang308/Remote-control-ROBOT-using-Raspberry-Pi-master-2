# Output pins of Metropolia's GPIO addon board
# O_P* should be used in the code.
# Numbers 3,5,... are Raspberry pi board pin numbers and they should not be changed unless you know the addon board layout

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Output pins
global O1
global O2
global O3
global O4
global O5
global O6
global O7
global O8
O1=9
O2=10
O3=22
O4=27
O5=17
O6=4
O7=3
O8=2

#Input pins
global I1
global I2
global I3
global I4
global I5
global I6
global I7
global I8
I1=20
I2=21
I3=26
I4=19
I5=13
I6=6
I7=5
I8=11

def initMetroPins():
	#output pins
	GPIO.setup(O1,GPIO.OUT)
	GPIO.setup(O2,GPIO.OUT)
	GPIO.setup(O3,GPIO.OUT)
	GPIO.setup(O4,GPIO.OUT)
	GPIO.setup(O5,GPIO.OUT)
	GPIO.setup(O6,GPIO.OUT)
	GPIO.setup(O7,GPIO.OUT)
	GPIO.setup(O8,GPIO.OUT)
	#Input pins
	GPIO.setup(I1,GPIO.IN)
	GPIO.setup(I2,GPIO.IN)
	GPIO.setup(I3,GPIO.IN)
	GPIO.setup(I4,GPIO.IN)
	GPIO.setup(I5,GPIO.IN)
	GPIO.setup(I6,GPIO.IN)
	GPIO.setup(I7,GPIO.IN)
	GPIO.setup(I8,GPIO.IN)



