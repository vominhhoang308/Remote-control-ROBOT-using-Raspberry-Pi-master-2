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
RF = GPIO.PWM(io.O1,100)
LF.start(0)
RF.start(0)

######## setMovingDirection ##########

t = 0.01
dc = 15
channel_1 = 11
channel_2 = 20
step = 0
dia = 207.345


##movement####
def forward(dc):
    LF.start(dc)
    RF.start(dc)
    time.sleep(t)

def idle():
    GPIO.output(io.O7, False)
    GPIO.output(io.O1, False)
    LF.start(0)
    RF.start(0)

##main func##

def thread_call(channel):
   global step
   step+=1
   print(step)

def rise_call():
   print ('RISE')


def run(step_run):
##   step_run = round((dist *1000) *16 / dia, 0)
   try:
       GPIO.add_event_detect(channel_1,GPIO.RISING, callback=thread_call)
##       GPIO.add_event_detect(channel_2,GPIO.RISING, callback=thread_call)
       while (step<step_run):
         forward(dc)
         time.sleep(0.02)
         idle()
   except KeyboardInterrupt:
       GPIO.cleanup()

time.sleep(13)
run(137)
GPIO.cleanup()
