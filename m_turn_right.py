# Right Turn Code

import RPi.GPIO as GPIO
import time
import serial

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)

IR_L = 2
IR_R = 3

LM1= 26
LM2= 19
RM1= 20
RM2= 16 

GPIO.setup(IR_L,GPIO.IN) #GPIO 2 -> Left IR out
GPIO.setup(IR_R,GPIO.IN) #GPIO 3 -> Right IR out

GPIO.setup(RM1,GPIO.OUT) #GPIO 4 -> Motor 1 terminal A
GPIO.setup(RM2,GPIO.OUT) #GPIO 14 -> Motor 1 terminal B

GPIO.setup(LM1,GPIO.OUT) #GPIO 17 -> Motor Left terminal A
GPIO.setup(LM2,GPIO.OUT) #GPIO 18 -> Motor Left terminal B


def turn_right():

    print("Right Turn Started")
    
    while(True):

        if(GPIO.input(IR_L)==False and GPIO.input(IR_R)==False):

            print(" Right Turn Correction")
            right_fun_main()
            break
            
        GPIO.output(RM1,False) #2A+
        GPIO.output(RM2,True) #2B-
        
        GPIO.output(LM1,True) #2A+
        GPIO.output(LM2,False) #2B

def right_fun_correction():

    print("Final Right Operation")
    
    while(True):

        if(GPIO.input(IR_L)==True and GPIO.input(IR_R)==True):

            break

        GPIO.output(RM1,True) #2A+
        GPIO.output(RM2,False) #2B-
        
        GPIO.output(LM1,False) #2A+
        GPIO.output(LM2,True) #2B-

    GPIO.output(RM1,True) #2A+
    GPIO.output(RM2,True) #2B-

    GPIO.output(LM1,True) #2A+
    GPIO.output(LM2,True) #2B-

    print("Right Turn Ended")


def right_fun_main():

    print(" Final Right Operation")
    
    while(True):

        if(GPIO.input(IR_L)==True and GPIO.input(IR_R)==True):

            break
        
        GPIO.output(RM1,False) #2A+
        GPIO.output(RM2,True) #2B-
        
        GPIO.output(LM1,True) #2A+
        GPIO.output(LM2,False) #2B-

    GPIO.output(RM1,True) #2A+
    GPIO.output(RM2,True) #2B-

    GPIO.output(LM1,True) #2A+
    GPIO.output(LM2,True) #2B-



    
    
