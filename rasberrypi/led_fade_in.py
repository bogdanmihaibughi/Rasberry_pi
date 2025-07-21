import RPi.GPIO as GPIO
import time

# Configurare GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

# Initializam PWM pe pinul LED-ului cu frecvența de 100Hz
pwm = GPIO.PWM(led_pin, 100)
pwm.start(0)  # Start la intensitate 0%

print("LED stins")

# Aprindere treptată
for duty_cycle in range(0, 101, 1):  # De la 0% la 100%
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.02) 

print("LED aprins complet")

pwm.stop()
GPIO.cleanup()
