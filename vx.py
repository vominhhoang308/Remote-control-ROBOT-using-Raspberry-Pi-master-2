import RPi.GPIO as GPIO

import time
import metroGPIO as io
import os



######## InitPins ###########
io.initMetroPins()



######## define pin #####
LB = GPIO.PWM(io.O8,100)
RF = GPIO.PWM(io.O1,100)
LF = GPIO.PWM(io.O7,100)
RB = GPIO.PWM(io.O2,100)
LF.start(0)
LB.start(0)
RF.start(0)
RB.start(0)
######## setMovingDirection ##########

t = 0.02

def idle():
        GPIO.output(io.O1, False)
	GPIO.output(io.O2, False)
        GPIO.output(io.O7, False)
	GPIO.output(io.O8, False)
        LF.start(0)
        LB.start(0)
        RF.start(0)
        RB.start(0)
        
def backward(dc,t):
	LB.start(dc)
        RB.start(dc)
	time.sleep(t)
    
def forward(dc,t):
	LF.start(dc)
        RF.start(dc)
	time.sleep(t)
	
def spin_left(dc,t):

        LB.start(dc)
        RF.start(dc)
	time.sleep(t)
	
def spin_right(dc,t):

        LF.start(dc)
        RB.start(dc)
	time.sleep(t)

######## Auto run  ##########
dc=20
t=3

##LF.start(20)
##time.sleep(3)
##idle()
##LB.start(20)
##time.sleep(3)
##idle()
##RF.start(20)
##time.sleep(3)
##idle()
##RB.start(20)
##time.sleep(3)
##idle()

t1=1.9/2.5*3.0
t2=1.15/2.5*3.0
time.sleep(13)


forward(20,t1)
time.sleep(t1)
idle()
time.sleep(3)
spin_right(20,0.23)
time.sleep(.23)
idle()
time.sleep(3)

forward(20,t2)
time.sleep(t2)
idle()
time.sleep(3)
spin_right(20,0.23)
time.sleep(.23)
idle()
time.sleep(3)

forward(20,t1)
time.sleep(t1)
idle()
time.sleep(3)
spin_right(20,0.23)
time.sleep(.23)
idle()
time.sleep(3)

forward(20,t2)
time.sleep(t2)
idle()
time.sleep(3)
spin_right(20,0.23)
time.sleep(.23)
idle()
time.sleep(3)

##backward(20,3)
##time.sleep(3)
##idle()
##
##time.sleep(5)
##spin_left(20,0.45)
##time.sleep(.45)
##idle()
##forward(60,2)
##time.sleep(t)
##idle()



GPIO.cleanup()


