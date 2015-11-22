import RPi.GPIO as GPIO
import curses
import time
import metroGPIO as io
import os
import picamera



########init curse###########
stdscr = curses.initscr() #init screen
curses.noecho() #turn off echo
curses.cbreak() #react keys instantly
stdscr.keypad(True) #enable keypad mode

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

dc=30
dcr=1.0*dc
t = 0.015

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

def camera()
        camera = picamera.PiCamera()
        try:
                while True:
                        camera.start_preview()
                        time.sleep(1000000)
        except KeyboardInterrupt:
	pass

def servo(sdeg):
##        if (sdeg>=0) and (sdeg<=90):
##                dc= 15-((90-sdeg)/9)
##        elif sdeg>90 and sdeg<=180:
##                dc= 15+((sdeg-90)/9)
        s=GPIO.PWM(io.O3,100)
        s.start(0)
##        s.ChangeDutyCycle(dc)
##        time.sleep(2)
        try:
            while True:
                s.ChangeDutyCycle(15)
                time.sleep(2)
                s.ChangeDutyCycle(25)
                time.sleep(2)
                s.ChangeDutyCycle(15)
                time.sleep(2)
                s.ChangeDutyCycle(5)
                time.sleep(2)
        except KeyboardInterrupt:
            GPIO.cleanup

######## Manual run  ##########

while True:
	c = stdscr.getch()
	if c == ord('w'):
		forward(dc,t)
		time.sleep(t)
		idle()
	elif c == ord('s'):
		backward(dc,t)
		time.sleep(t)
		idle()
	elif c == ord('a'):
		spin_left(dc,t)
		time.sleep(t)
		idle()
	elif c == ord('d'):
		spin_right(dc,t)
		time.sleep(t)
		idle()
	elif c == ord('h'):
		try:
			if dc<=95:
				dc+=5
				stdscr.addstr("DC: ", dc )
		except curses.error:
			pass	
	elif c == ord('l'):
		try:
			if dc>=5:
				dc-=5
				stdscr.addstr("DC:", dc )
		except curses.error:
			pass
	elif c == ord('m'):
		servo(90)
		
	elif c == ord('c'):
		camera()
		
	elif c == 0x27:
		break


#######terminate curses######
stdscr.keypad(False)
curses.nocbreak()
curses.echo()
curses.endwin()





GPIO.cleanup()


