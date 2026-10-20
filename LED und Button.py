#from machine import Pin
#from time import sleep

#LED_PIN = 15

#led_Pin = Pin(LED_PIN, Pin.OUT, value = 1)

#while True:
    #led_Pin.value(not led_Pin.value())
    #sleep(0.5)




#from machine import Pin

#LED_PIN = 15
#BUTTON = 2

#led = Pin(LED_PIN, Pin.OUT, value = 0)
#button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)

##PullUp = oben = 1
##0 = gedrückt

#while True:
   # if button.value() == 0:
        #led.value(1)
   

from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT, value = 0)
button = Pin(2, Pin.IN, Pin.PULL_UP)

sleep(1)

while True:
    if button.value() == 0:
        led.value(1)
        sleep(1)