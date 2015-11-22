import RPi.GPIO as GPIO
import sys, tty, termios
import time
import metroGPIO as io
import os
import math
######## InitPins ###########
io.initMetroPins()

######## define pin #####
LF = GPIO.PWM(io.O7,100)
import RPi.GPIO as GPIO
import sys, tty, termios
import time
import metroGPIO as io
import os
import math
######## InitPins ###########
io.initMetroPins()

######## define pin #####
LF = GPIO.PWM(io.O7,100)
LB = GPIO.PWM(io.O8,100)
RF = GPIO.PWM(io.O1,100)
RB = GPIO.PWM(io.O2,100)
LF.start(0)
LB.start(0)
RF.start(0)
RB.start(0)
######## setMovingDirection ##########

t = 0.01
dc = 30
dcr=1.0*dc
channel_1 = 11
channel_2 = 20
step = 0
dia = 207.345

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
        RB.start(dcr)
	time.sleep(t)
    
def forward(dc,t):
	LF.start(dc)
        RF.start(dcr)
	time.sleep(t)
	
def spin_left(dc,t):

        LB.start(dc)
        RF.start(dc)
	time.sleep(t)
	
def spin_right(dc,t):

        LF.start(dc)
        RB.start(dc)
	time.sleep(t)
    

##main func##

def thread_call(channel):
   global step
   step+=1
   print(step)

def rise_call():
   print ('RISE')


def run(opt,dist):
   	#real_dist= 1.25*dist - 0.0791 #at dc= 15
	real_dist= 1.2345679*dist - 0.1358  #at dc= 30
	#real_dist = dist	
   	step_run = round((real_dist *1000) *16 / dia, 0)
   	try:
       		GPIO.add_event_detect(channel_1,GPIO.RISING, callback=thread_call)
     		#GPIO.add_event_detect(channel_2,GPIO.RISING, callback=thread_call)
       		while (step<=step_run):
			if opt == 1:
				forward(dc,t)
			elif opt == -1:
				backward(dc,t)
			time.sleep(0.02)
        		idle()
   	except KeyboardInterrupt:
       		GPIO.cleanup()

def turn(opt,deg):
	real_deg = deg - 30 #Degree calculation
	step_run = round(deg*2.5/20)
	try:
       		#GPIO.add_event_detect(channel_1,GPIO.RISING, callback=thread_call)
     		GPIO.add_event_detect(channel_2,GPIO.RISING, callback=thread_call)
       		while (step<=step_run):
			if opt == 1:
				spin_left(dc,t)
			elif opt == -1:
				spin_right(dc,t)
         		time.sleep(0.02)
         		idle()
   	except KeyboardInterrupt:
       		GPIO.cleanup()

dist=3
deg=9
time.sleep(0)
run(-1,dist)
#GPIO.cleanup()
#time.sleep(1)
#run(-1,dist)
#GPIO.cleanup()
#turn(-1,180)
GPIO.cleanup()

