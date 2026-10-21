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
#led_r2 = Pin(LED_R2, Pin.OUT, value = 0)
#led_g2 = Pin(LED_G2, Pin.OUT, value = 0)
led_b = Pin(LED_B, Pin.OUT, value = 0)
btn1 = Pin(BTN1, Pin.IN, Pin.PULL_UP)
btn2 = Pin(BTN2, Pin.IN, Pin.PULL_UP)
bar = Pin(BAR,Pin.IN, Pin.PULL_DOWN)

state0 = 0 # car outside
state1 = 1 # barrier open
state2 = 2 # car inside
state3 = 3 # barrier open
current_state = state0

anzahl = 0
maximun = 4

#btn1_state_old = btn.value()
#btn2_state_old = btn.value()
print(btn1.value())
print(bar.value())
while True:
    tick_new = time.ticks_ms()
    #btn1_state_new = btn.value()
    #btn2_state_new = btn.value()
    
    # conditions
    if current_state == state0:
        #if btn1_state_old == 1 and btn1_state_new == 0:
        if btn1.value() == 0:
            if anzahl < maximum:
                current_state = state1
                tick_old = time.ticks_ms()
                led_b.value(1)
            #btn_state_old = btn_state_new
        #elif btn1_state_old == 1 and btn1_state_new == 1:
            #btn_state_old = btn_state_new
    elif current_state == state1:
        if bar.value() == 1:
            current_state = state2
            anzahl +=1
    elif current_state == state2:
        #if btn2_state_old == 1 and btn2_state_new == 0:
        if btn2.value() == 0:
            current_state = state3
            #btn_state_old = btn_state_new
        #elif btn2_state_old == 1 and btn2_state_new == 1:
            #btn_state_old = btn_state_new
    elif current_state == state3:
        if bar.value() == 1:
            current_state = state0
            anzahl -= 1
    
    
    # actions
    if current_state == state0:
        led_r1.value(1)
        led_ge.value(0)
        led_g1.value(0)
        led_b.value(0)
    if current_state == state1:
        led_r1.value(0)
        led_ge.value(1)
        led_g1.value(0) 
        if time.ticks_diff(tick_new, tick_old) >= 2000:
            led_b.value(0)
            tick_old = tick_new
    if current_state == state2:
        led_r1.value(0)
        led_ge.value(0)
        led_g1.value(1)
        led_b.value(0)
    if current_state == state3:
        led_r1.value(0)
        led_ge.value(1)
        led_g1.value(0)
        led_b.value(0)
    #print(current_state)
        
        
    

 



      
      