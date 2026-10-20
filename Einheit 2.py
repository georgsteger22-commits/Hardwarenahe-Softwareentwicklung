from machine import Pin
import time

led = Pin(15, Pin.OUT)
btn1 = Pin(4, Pin.IN, Pin.PULL_UP)
btn2 = Pin(5, Pin.IN, Pin.PULL_UP)

# State Machine
STATE_OFF = 0
STATE_ON = 1
current_state = STATE_OFF

print(btn1.value())
print(btn2.value())
print(led.value())

while True:
    # Übergänge
    if current_state == STATE_OFF:
        if btn1.value() == 0:
            current_state = STATE_ON
            print("off -> on")
    elif current_state == STATE_ON:
        if btn2.value() == 0:
            current_state = STATE_OFF
            print("on -> off")
    
    # Actions
    if current_state == STATE_OFF:
        led.value(0)
    elif current_state == STATE_ON:
        led.value(1)
    