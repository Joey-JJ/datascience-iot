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
    
    # Creating File and Writing headers
    with open('data.csv', 'w') as file:
        file.write('Time, Temp (C), Humidity (%)\n')
        try:
            while True:
                # Reading values from sensor
                result = instance.read()
                if result.is_valid():
                    # Storing instance values
                    current_time = datetime.datetime.now()
                    temperature = str(result.temperature)
                    humidity = str(result.humidity)
                    
                    # Printing data
                    print(f'Last valid input: {str(datetime.datetime.now())}')
                    print(f'Temperature: {result.temperature}C')
                    print(f'Humidity: {result.humidity}%')
                    
                    # Writing data to file
                    file.write(f'{str(current_time)}, {temperature}, {humidity}\n')
                 
                # Waiting 5 seconds per measurements
                time.sleep(5)

        except KeyboardInterrupt:
            print('Cleanup')
            GPIO.cleanup()

if __name__ == '__main__':
    main()
