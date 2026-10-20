from machine import Pin
import time

# 1. state = dauerlicht
# 2. state = blinken

btn = Pin(5, Pin.IN, Pin.PULL_UP)
led = Pin(4, Pin.OUT, value=1)

state0 = 0 # nicht gedrückt (leuchten)
state1 = 1 # gedrückt (blinken)
current_state = state0

last_tick = time.ticks_ms()

last_btn = btn.value()

while True:
    this_btn = btn.value()
    if current_state == state0:
        if last_btn == 1 and this_btn == 0:
            current_state = state1
            last_btn = this_btn
        elif last_btn == 0 and this_btn == 1:
            last_btn = this_btn
            
    elif current_state == state1:
        if last_btn == 1 and this_btn == 0:
            current_state = state0
            last_btn = this_btn
        elif last_btn == 0 and this_btn == 1:
            last_btn = this_btn
    
    now = time.ticks_ms()
    
    if current_state == state0:
        led.value(1)
    
    elif current_state == state1:
        if time.ticks_diff(now, last_tick) >= 200:
            led.value(not led.value())
            last_tick = now
