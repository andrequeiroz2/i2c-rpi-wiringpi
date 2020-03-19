import wiringpi as wiringpi
from waiting import wait, TimeoutExpired 
from time import sleep 
 
state = 1
pin_base = 65       # lowest available starting number is 65  
i2c_addr = 0x20     # A0, A1, A2 pins all wired to GND  
  
wiringpi.wiringPiSetup()                    # initialise wiringpi  
wiringpi.mcp23017Setup(pin_base,i2c_addr)   # set up the pins and i2c address  
  
wiringpi.pinMode(65, 1)         # sets GPA0 to output  
wiringpi.digitalWrite(65, 0)    # sets GPA0 to 0 (0V, off)  
  
wiringpi.pinMode(72, 0)         # sets GPB7 to input  
wiringpi.pullUpDnControl(72, 2) # set internal pull-up   
  
try:  
    while True:  
        if wiringpi.digitalRead(72):  
          if state == 1:
            while wiringpi.digitalRead(72):
              wait(lambda: True)
              wiringpi.digitalWrite(65, 1) # sets port GPA1 to 1 (3V3, on)
              state = 0 
          else:
            while wiringpi.digitalRead(72):
              wait(lambda: True)
              wiringpi.digitalWrite(65, 0) # sets port GPA1 to 0 (0V, off)
              state = 1
finally:  
    wiringpi.digitalWrite(65, 0) # sets port GPA1 to 0 (0V, off)  
    wiringpi.pinMode(65, 0)      # sets GPIO GPA1 back to input Mode