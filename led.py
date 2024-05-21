from gpiozero import LED, PWMLED
from time import sleep

green = PWMLED(17)
while True:
    green.value = 0
    sleep(0.5)
    green.value = 0.5
    sleep(0.5)
    green.value = 1
    sleep(0.5)
    