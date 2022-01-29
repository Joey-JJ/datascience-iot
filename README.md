# Measure temperature and air humidity with the raspberry pi and DHT11/DHT22

![alt](https://github.com/Joey-JJ/datascience-iot/blob/main/assets/setup.jpg)

This project collects data about temperature and air humidity. The data is written to a csv file, which can be used to perform analysis and gain insights from the data. 

## Requirements
### Hardware
![alt](https://github.com/Joey-JJ/datascience-iot/blob/main/assets/requirements.jpg)
1. DHT11 (or DHT22) sensor
2. Raspberry Pi 4 (Model B)
3. 3 Female-to-female jumper cables
4. SD-card (8GB minimal)
5. Keyboard/Mouse (Optional)
6. Monitor (Optional)

### Software
1. Raspberry Pi OS (with an IDE if you're not using SSH)
2. Tool to analyse data from CSV files (for example Excel, Google Sheets, Jupyter Notebooks, etc.)

## Set up
### Step 1: Install Raspberry Pi OS
Download the 'Raspberry Pi Imager' from https://www.raspberrypi.com/software/. Choose 'Raspberry Pi OS (32-bit) as the Operating System, and choose your micro SD card as 'storage'. Click 'Write' and wait untill the process is done. Insert the SD card into the Raspberry Pi and follow the set up process. Once set up is done, update the OS by entering the following commands into the terminal:
```bash
sudo apt-get update
```

```bash
sudo apt-get upgrade
```

### Step 2: Connect the sensor to the Raspberry Pi
![alt](https://github.com/Joey-JJ/datascience-iot/blob/main/assets/dht11_with_cables.jpg)
As you can see on the picture, the sensor has 3 labelled pins: VCC, DATA and GND. Connect your three jumper cables to the pins. The cable connected to VCC should go to a 5V power output pin (in my case I used a 5V pin, pin number 2). The DATA cable should go to a GPIO pin (I used pin 7) and the GND cable should go to a ground pin (I used pin 6). If everything is connected properly, the LED on the sensor should turn on (as seen on the first picture).


### Step 3: Install necessary libraries
The only library needed is the 'dht11' library. Install it by entering the following command into the terminal: 
```bash
pip install dht11
```

### Step 4: Test the set up
Open up an IDE to test if everything is set up correctly. You can use the following Python code to test if your sensor is outputting data:
```py
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
    instance = dht11.DHT11(pin=4) # CHANGE THE PIN NUMBER IF YOU'RE USING A DIFFERENT PIN

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
```
If everything is working correctly, readings should be printed to the console.

### Step 5: Start collecting data
I modified the code above so it will store each correct reading inside a CSV file. The code will create a CSV file named 'data.csv', and it will store everything there. You can collect data over a period of time, and then stop by hitting 'CTRL/Command + C' on your keyboard. Here is my code:
```py
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
    instance = dht11.DHT11(pin=4)       # CHANGE THE PIN NUMBER IF YOU USE A DIFFERENT PIN
    
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
```
An example of the data can be found in the directory 'data' in this repository. There is also an example of the analysis I did on the data.

## Data Pipeline
![alt](https://github.com/Joey-JJ/datascience-iot/blob/main/assets/data_pipeline.jpg)

Data is collected by the sensor and saved in a CSV file. To collect the data, send the CSV file to your desired location. Visualize data with your tool of choice.

## Sources
1. https://github.com/szazo/DHT11_Python/blob/master/README.md
2. https://www.youtube.com/watch?v=KUr8WgSIsfk&t=203s
