import picamera
import time

camera = picamera.PiCamera()


### Preview ###
#camera.start_preview()
#camera.stop_review()

### Camera settings with default values###
#camera.brightness = 70
#camera.sharpness = 0
#camera.contrast = 0
#camera.saturation = 0
#camera.ISO = 0
#camera.video_stabilization = False
#camera.exposure_compensation = 0
#camera.exposure_mode = 'auto'
#camera.meter_mode = 'average'
#camera.awb_mode = 'auto'
#camera.image_effect = 'none'
#camera.color_effects = None
#camera.rotation = 0
#camera.hflip = False
#camera.vflip = False
#camera.crop = (0.0,0.0,1.0,1.0)


### Capture images ###
#camera.capture('image1.jpg')
#sleep(5)

### Video recording ###
#camera.start_recording('video1.h264')
#camera.stop_recording()

try:
	while True:
		camera.start_preview()
		time.sleep(10000)
except KeyboardInterrupt:
	pass

#camera.start_recording('video1.h264')
#time.sleep(90)

