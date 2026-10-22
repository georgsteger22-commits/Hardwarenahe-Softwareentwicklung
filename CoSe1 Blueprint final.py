from machine import Pin
import time

# Pins
PIN_BUTTON = 5
PIN_LS= 4
PIN_LED_CAR_RED = 23
PIN_LED_CAR_YELLOW = 22
PIN_LED_CAR_GREEN = 21
PIN_LED_PED_RED = 26
PIN_LED_PED_GREEN = 27

# Hardware
btn1 = Pin(PIN_BUTTON, Pin.IN, Pin.PULL_UP)
ls = Pin(PIN_LS, Pin.IN, Pin.PULL_UP)
led_car_red = Pin(PIN_LED_CAR_RED, Pin.OUT)
led_car_yellow = Pin(PIN_LED_CAR_YELLOW, Pin.OUT)
led_car_green = Pin(PIN_LED_CAR_GREEN, Pin.OUT)
led_ped_red = Pin(PIN_LED_PED_RED, Pin.OUT)
led_ped_green = Pin(PIN_LED_PED_GREEN, Pin.OUT)

state0 = 0 # Autoampel rot
state1 = 1 # Autoampel gelb
state2 = 2 # Autoampel grün
state3 = 3 # Knopf gedrückt
current_state = state0

tick_old = time.ticks_ms()

def all_leds_off():
    led_car_red.value(0)
    led_car_green.value(0)
    led_car_yellow.value(0)
    led_ped_red.value(0)
    led_ped_green.value(0)

while True:
    
    tick_new = time.ticks_new()
    
    # Definitions
    if current_state == state0:
        if : # Übergangskondition erreicht
            current_state = state1
    elif current_state == state1:
        if :
            current_state = state2
    elif current_state == state2:
        if :
            current_state = state3
    elif current_state == state3:
        if :
            current_state = state0
    
    # Actions
    if current_state == state0:
        all_leds_off()
        led_car_red.value(1)
        led_ped_green.value(1)
    elif current_state == state1:
        all_leds_off()
        led_car_yellow.value(1)
    elif current_state == state2:
        all_leds_off()
        led_car_green.value(1)
        led_ped_red.value(1)
    elif current_state == state3:
        all_leds_off()
        

# Zeitmessung z.B. für blinken
old_time = time.ticks_ms()
while True:
    new_time = time.ticks_ms()
    if time.ticks_diff(new_time, start_time) >= 1000:
        # ...
        old_time = new_time


# Flankenmessung vom Button
last_btn_state = btn.value() #nicht gedrückt = 1
while True:
    new_btn_state = btn.value()
    if new_btn_state == 0 and new_btn_state != old_btn_state:
        # ...
    last_btn_state = new_btn_state
    

# Lichtschranke
# ohne Lichtunterbechung = 0
if ls.value() == 1:
    # Licht unterbrochen


# Achtung!!!
ledx.value(not led.value()) # zweiten Klammern nicht vergessen


