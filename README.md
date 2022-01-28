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
As you can see on the picture, the sensor has 3 labelled pins: VCC, DATA and GND. Connect your three jumper cables to the pins. The cable connected to VCC should go to a 5V power output pin (in my case I used a 5V pin, pin number 2). The DATA cable should go to a GPIO pin (I used pin 7) and the GND cable should go to a ground pin (I used pin 6). If everything is connected properly, the LED on the sensor should turn on.

### Step 3: Install necessary libraries
The only library needed is the 'dht11' library. Install it by entering the following command into the terminal: 
```bash
pip install dht11
```
