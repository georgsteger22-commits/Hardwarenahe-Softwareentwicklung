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
led_ge1 = Pin(LED_GE1, Pin.OUT, value = 0)
led_g1 = Pin(LED_G1, Pin.OUT, value = 0)
led_r2 = Pin(LED_R2, Pin.OUT, value = 0)
led_g2 = Pin(LED_G2, Pin.OUT, value = 0)
led_b = Pin(LED_B, Pin.OUT, value = 0)
btn1 = Pin(BTN1, Pin.IN, Pin.PULL_UP)
btn2 = Pin(BTN2, Pin.IN, Pin.PULL_UP)
bar = Pin(BAR,Pin.IN, Pin.PULL_DOWN)

state0 = 0
state1 = 1
current_state = state0

# Button: Pin.PULL_UP == 1
# gedrückt == 0

# Barrier: Pin.PULL_DOWN == 0
# unterbrechung der Schranke == 1

