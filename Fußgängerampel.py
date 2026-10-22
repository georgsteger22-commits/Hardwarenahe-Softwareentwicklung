from machine import Pin
import time

LED_R1 = 5
LED_GE1 = 18
LED_G1 = 19
LED_R2 = 27
LED_G2 = 25
LED_B = 23
BTN1 = 33
BTN2 = 32
BAR = 4

led_r1 = Pin(LED_R1, Pin.OUT, value = 0)
led_ge = Pin(LED_GE1, Pin.OUT, value = 0)
led_g1 = Pin(LED_G1, Pin.OUT, value = 0)
led_r2 = Pin(LED_R2, Pin.OUT, value = 0)
led_g2 = Pin(LED_G2, Pin.OUT, value = 0)
led_b = Pin(LED_B, Pin.OUT, value = 0)
btn1 = Pin(BTN1, Pin.IN, Pin.PULL_UP)
btn2 = Pin(BTN2, Pin.IN, Pin.PULL_UP)
bar = Pin(BAR,Pin.IN, Pin.PULL_DOWN)

state0 = 0 # Autos stehen
state1 = 1 # Ampel rot-gelb
state2 = 2 # Autos fahren
state3 = 3 # Ampel gelb
state4 = 4 # Nachtmodus

current_state = state0

tick_old = time.ticks_ms()
btn_state_old = btn1.value()

btn1_pressed = False
btn2_pressed = False

while True:
    tick_new = time.ticks_ms()
    btn_state_new = btn1.value()
    
    if btn2.value() == 0:
        current_state == state4
    
    elif current_state == state0:
        
        if time.ticks_diff(tick_new, tick_old) >= 7000 and btn2_pressed == True:
            current_state = state4
            btn2_pressed = False
        elif time.ticks_diff(tick_new, tick_old) >= 7000:
            current_state = state1
            tick_old = tick_new
    elif current_state == state1:
        if time.ticks_diff(tick_new, tick_old) >= 1000:
            current_state = state2
            tick_old = tick_new
    elif current_state == state2:
        if btn_state_new == 0 and btn_state_new != btn_state_old:
            btn1_pressed = True
            if time.ticks_diff(tick_new, tick_old) >= 200:
                led_b.value(not led_b.value())
        if time.ticks_diff(tick_new, tick_old) >= 10000 or time.ticks_diff(tick_new, tick_old) >= 7000 and btn1_pressed == True:
            current_state = state3
            tick_old = tick_new
            btn1_pressed = False
            led_b.value(0)
    elif current_state == state3:
        if time.ticks_diff(tick_new, tick_old) >= 2000:
            current_state = state0
            tick_old = tick_new
    elif current_state == state4:
        if btn2.value() == 0:
            current_state = state0
            tick_old = tick_new
        elif btn1.value() == 0:
            current_state = state3
            btn2_pressed = True
            
    if current_state == state0:
        led_r1.value(1)
        led_ge.value(0)
        led_g1.value(0)
        led_r2.value(0)
        led_g2.value(1)
        led_b.value(0)
    elif current_state == state1:
        led_r1.value(1)
        led_ge.value(1)
        led_g1.value(0)
        led_r2.value(1)
        led_g2.value(0)
        led_b.value(0)
    elif current_state == state2:
        led_r1.value(0)
        led_ge.value(0)
        led_g1.value(1)
        led_r2.value(1)
        led_g2.value(0)
        led_b.value(0)
    elif current_state == state3:
        led_r1.value(0)
        led_ge.value(1)
        led_g1.value(0)
        led_r2.value(1)
        led_g2.value(0)
        led_b.value(0)
    elif current_state == state4:
        led_r1.value(0)
        # led_ge.value(0)
        led_g1.value(0)
        led_r2.value(1)
        led_g2.value(0)
        led_b.value(0)
        if time.ticks_diff(tick_new, tick_old) >=200:
            led_ge.value(not led_ge.value())


