
import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False) ## Warning for used channels

## Let's activate the pins in order to use
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) ## In order to use the pin as output

while True:
    try:
        ## If you enter the right word then the light goes on
        question = input("Enter 'On' to turn the light on or 'Quit' to terminate the program: ")
        if question == "On" or question == "on":
            GPIO.output(18, 1) ##GPIO.HIGH
            print("Right output, the light is on\n")
            question = input("Enter 'Off' to turn the light off or 'Quit' to terminate the program: ")
            if question == "Off" or question == "off":
                GPIO.output(18, 0)
                print("Right output, the light is off\n")
            elif question == "Quit" or question == "quit" or question == 'q':
                GPIO.cleanup()
                sys.exit("The program is terminated!")
            else:
                print("You did not enter the right word")
                print("Wrong answer, the light is blinking")
                for i in range(1, 7):
                    GPIO.output(18, 1) ##GPIO.LOW
                    time.sleep(.5)
                    GPIO.output(18, 0)
                    time.sleep(.5)
        elif question == "Quit" or question == "quit" or question == 'q':
            GPIO.cleanup()
            sys.exit("The program is terminated!")
        else:
            print("You did not enter the right word")
            print("Wrong answer, the light is blinking")
            for i in range(1, 7):
                GPIO.output(18, 1) ##GPIO.LOW
                time.sleep(.5)
                GPIO.output(18, 0)
                time.sleep(.5)
    except KeyboardInterrupt:
        print("You pressed Ctrl + Z")
        GPIO.cleanup()
        sys.exit()
