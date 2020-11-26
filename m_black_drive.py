# Black Drive Code

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

TRIG = 23
ECHO = 24  

GPIO.setup(IR_L,GPIO.IN) #GPIO 2 -> Left IR out
GPIO.setup(IR_R,GPIO.IN) #GPIO 3 -> Right IR out

GPIO.setup(RM1,GPIO.OUT) #GPIO 4 -> Motor 1 terminal A
GPIO.setup(RM2,GPIO.OUT) #GPIO 14 -> Motor 1 terminal B

GPIO.setup(LM1,GPIO.OUT) #GPIO 17 -> Motor Left terminal A
GPIO.setup(LM2,GPIO.OUT) #GPIO 18 -> Motor Left terminal B


GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)

def dist():                           
          GPIO.output(TRIG, True)                  #Set TRIG as HIGH
          time.sleep(0.00001)                      #Delay of 0.00001 seconds
          GPIO.output(TRIG, False)                 #Set TRIG as LOW
          while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
            pulse_start = time.time()              #Saves the last known time of LOW pulse
          while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
            pulse_end = time.time()                #Saves the last known time of HIGH pulse 
          pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
          distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
          distance = round(distance, 2)            #Round to two decimal points
          return distance

        
def black_drive():

    try:

        print("Black Drive Started")
    
        while(True):

            if(dist()<15):
            
                print "Obstacle - ",dist()
                GPIO.output(RM1,True) #2A+
                GPIO.output(RM2,True) #2B-
                GPIO.output(LM1,True) #2A+
                GPIO.output(LM2,True) #2B-
                time.sleep(5)
            
            if(GPIO.input(IR_L)==True and GPIO.input(IR_R)==True):

                GPIO.output(RM1,True) #2A+
                GPIO.output(RM2,False) #2B-
                GPIO.output(LM1,True) #2A+
                GPIO.output(LM2,False) #2B-

            elif(GPIO.input(IR_L)==True and GPIO.input(IR_R)==False):

                GPIO.output(LM1,False) #2A+
                GPIO.output(LM2,True) #2B-

            elif(GPIO.input(IR_L)==False and GPIO.input(IR_R)==True):

                GPIO.output(RM1,False) #2A+
                GPIO.output(RM2,True) #2B-
        
            elif(GPIO.input(IR_L)==False and GPIO.input(IR_R)==False):

                GPIO.output(RM1,True) #2A+
                GPIO.output(RM2,True) #2B-
                GPIO.output(LM1,True) #2A+
                GPIO.output(LM2,True) #2B-
    
                break

        print("Black Drive Ended")

    except:
        print("Error Occured")

        GPIO.output(RM1,True) #2A+
        GPIO.output(RM2,True) #2B-
        GPIO.output(LM1,True) #2A+
        GPIO.output(LM2,True) #2B-
