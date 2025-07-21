
import signal
import sys
import RPi.GPIO as GPIO
import time

Buton_pieton = 26
Rosu_vehicul=14
Verde_vehicul=23
Rosu_pieton=12
Verde_pieton=16

def signal_handler(sig, frame):  #se executa la apasarea CTRL-C
    GPIO.cleanup()  #anuleaza configurarea GPIO
    sys.exit(0)



def semafor_pieton_activ():
    
    GPIO.output(Verde_vehicul,0)
    GPIO.output(Rosu_vehicul,1)
    GPIO.output(Verde_pieton,1)
    GPIO.output(Rosu_pieton,0)
    for i in range(0,5):
          time.sleep(1)
          print(5-i)     
    for i in range(0,5):  #intermitent
       GPIO.output(Verde_pieton,1)
       time.sleep(0.5)
       GPIO.output(Verde_pieton,0)
       time.sleep(0.5)

def semafor_pieton_inactiv():
     GPIO.output(Verde_vehicul,1)
     GPIO.output(Rosu_vehicul,0)
     GPIO.output(Verde_pieton,0)
     GPIO.output(Rosu_pieton,1)

     for i in range(0,10):
       time.sleep(1)    
       print(10-i)
   
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(Rosu_vehicul,GPIO.OUT)
GPIO.setup(Verde_vehicul,GPIO.OUT)
GPIO.setup(Rosu_pieton,GPIO.OUT)
GPIO.setup(Verde_pieton,GPIO.OUT)
GPIO.setup(Buton_pieton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#la apasarea CTRL-C se va executa functia signal_handler     
    
signal.signal(signal.SIGINT, signal_handler)
   
    
while True: 
     semafor_pieton_inactiv()   #starea S1
     
     semafor_pieton_activ()    #starea S2
    