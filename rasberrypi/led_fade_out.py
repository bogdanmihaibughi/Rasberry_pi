import RPi.GPIO as GPIO
import time

# Configurare GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

# Inițializăm PWM pe pinul LED-ului cu frecvența de 100Hz
pwm = GPIO.PWM(led_pin, 100)
pwm.start(100)  # Start la intensitate 100% (lumina maximă)

print("LED aprins")

# Stingere treptată
for duty_cycle in range(100, -1, -1):  # De la 100% la 0%
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.02)  # Timp între pași – ajustează pentru viteză mai lentă/rapidă

print("LED stins complet")

pwm.stop()
GPIO.cleanup()