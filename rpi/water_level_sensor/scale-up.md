# River level sensor network
Previously you used a rpi to serve a website that published river levels. The rpi does not have analog pins so we used a microbit to send the converted analog signal to the pi over serial communication. You used the flask framework to build a working website in html. You did all of this remotely over SSH.

What are the limitations of this setup?
- Scaleability
- Cost
- Setup

In this workshop we are going to look at The Internet of Things paradigm and how we can use it to improve our sensing setup

## Objectives
- Young coders can demonstrate competence using the commnad line
- Young coders can explain IOT
- Young coders can list network protocols
- Young coders can explain ssh and demonstate using it
- Young coders can differetiate between micro controller and micro processors
- Young coders can know where to find documentation
- Young coders can apply what they have learnt and list future iot projects
- Young coders can explain analog and digital sensors
- Young coders can find pin diagrams and locate io pins for the appropriate sensor

## Concepts
- IOT
- MQTT with mosquito
- SSH
- Command Line
- Inputs and Outputs
- Flask

## Tech
- Raspberry pi
- Pi pico
- Water level sensor
- Servo

## Links
 - [Mosquitto](https://mosquitto.org/)
 - [Web server](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask)
 - [Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
 - [Adafruit io prof Gallerger ](https://www.youtube.com/watch?v=H0IetHFuz98)
 - [Pico review](https://www.youtube.com/watch?v=cK9TnktZESM)


## Steps
- 1.) Setup pi, update, upgrade, connect to wifi
- 2.) Setup pi pico and run hello world(blink_led)
  - a. blink led
  - b. Find/use analog pin and wire up the water level
  - c. Read analog value
  - d. Setup wifi and test get some data and print it
  - e. Setup mosquitto or adafruit io and test subscribe and publish
 
## 1.) PI

Connect pi to HDMI, power, mouse and key board.

Check wifi connection

Lets update and upgrade the os 

Check your ip address ``` hostname -I ```

Return back to PC, run putty and connect over ssh to your pi using your ip address

Try to find the pi with your folder on it and swap with each other


## 2.) Pi pico

The pi pico is a powerful microcontroller, it might be small but it has a lot of potential.

``` text
  Form factor: 21 mm × 51 mm
  CPU: Dual Arm Cortex-M33 or dual RISC-V Hazard3 processors @150MHz
  Memory: 520 KB on-chip SRAM; 4 MB on-board QSPI flash
  Connectivity: 2.4GHz 802.11n wireless LAN and Bluetooth 5.2
  Interfacing: 26 multi-purpose GPIO pins, including 4 that can be used for ADC
  Peripherals:
      2 × UART
      2 × SPI controllers
      2 × I2C controllers
      24 × PWM channels
      1 × USB 1.1 controller and PHY, with host and device support
      12 × PIO state machines
```

What are GPIO pins for?
Can we connect an analog sensor?
Does the pico have wifi capabilities and how do you know if your board does?
Compare and list the differences between a pico and a rpi-4/5?

### a.) 
First things first we must test our pico is working

Traditionally, we print 'Hello World' to the console; however, the microcontroller equivalent is to blink an LED as well.
Every board has an onboard led and that is a simple built in periphiral to access.

```python

```





