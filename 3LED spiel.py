from machine import Pin
import time

LED_R = 23
LED_B = 22
LED_G = 21
BTN1 = 4
BTN2 = 5

led_R = Pin(LED_R, Pin.OUT, value = 0)
led_B = Pin(LED_B, Pin.OUT, value = 0)
led_G = Pin(LED_G, Pin.OUT, value = 0)
btn1 = Pin(BTN1, Pin.IN, Pin.PULL_UP)
btn2 = Pin(BTN2, Pin.IN, Pin.PULL_UP)

# Beschreibung des Ablaufs
# wenn kein button gedrückt, dann rotes licht
# ein button = blaues licht
# beide buttons = grünes Licht

state_R = 0
state_B = 1
state_G = 2
current_state = state_R

while True:
    # Conditions
    if current_state == state_R:
        if btn1.value() == 0 or btn2.value() == 0:
            current_state = state_B
        elif btn1.value() == 0 and btn2.value() == 0:
            current_state = state_G
    elif current_state == state_B:
        if btn1.value() == 0 and btn2.value() == 0:
            current_state = state_G
        elif btn1.value() == 1 and btn2.value() == 1:
            current_state = state_R
    elif current_state == state_G:
        if btn1.value() == 1 and btn2.value() == 1:
            current_state = state_R
        elif btn1.value() == 0 and btn2.value() == 1 or btn1.value() == 1 and btn2.value() == 0:
            current_state = state_B
    
    # Actions
    if current_state == state_R:
        led_R.value(1)
        led_B.value(0)
        led_G.value(0)
    elif current_state == state_B:
        led_R.value(0)
        led_B.value(1)
        led_G.value(0)
    elif current_state == state_G:
        led_R.value(0)
        led_B.value(0)
        led_G.value(1)