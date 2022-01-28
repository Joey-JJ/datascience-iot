# Necessary imports
import dht11
import RPi.GPIO as GPIO
import time
import datetime


def main() -> None:
    # Setting GPIO settings
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
  
    # Initialising sensor instance
    instance = dht11.DHT11(pin=4)

    try:
        while True:
            # Reading values from sensor
            result = instance.read()
            # Checking if reading is valid
            if result.is_valid():
                # Printing data
                print(f'Last valid input: {str(datetime.datetime.now())}')
                print(f'Temperature: {result.temperature}C')
                print(f'Humidity: {result.humidity}%')
               
             # Waiting for 5 seconds to get next reading
            time.sleep(5)

    except KeyboardInterrupt:
        print('Cleanup')
        GPIO.cleanup()

        
if __name__ == '__main__':
    main()
