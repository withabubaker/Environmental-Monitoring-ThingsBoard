# Real-Time Environmental Monitoring with BLE Sensors and MQTT
![alt text](https://github.com/withabubaker/Environmental-Monitoring-ThingsBoard/blob/main/img/TBdashboard.jpg)

An inexpensive and efficient way to stream temperature and humidity data in real-time. This project uses open-source Pareto Anywhere middleware to fetch data from Minew S1 BLE sensor, then pushes the readings to a ThingsBoard dashboard via the MQTT protocol. It also supports sending alerts via AWS SNS based on temperature or humidity thresholds, making it ideal for smart buildings, labs, or manufacturing environments. 

## Project Goals:

- Use Pareto Anywhere to capture temperature and humidity data from the Minew S1 BLE Sensor.
- Send the data to ThingsBoard via the MQTT protocol.
- Display the data on the ThingsBoard dashboard.
- Send SMS notifications via AWS SNS based on temperature or humidity thresholds.


## Tools & Devices:

1. Raspberry Pi4.
2. [Pareto Anywhere](https://www.reelyactive.com/pareto/anywhere/).
3. [Minew S1 BLE Sensor](https://www.minew.com/product/s1-ble-temperature-and-humidity-sensor/).
4. [ThingsBoard installed locally on Pi4](https://thingsboard.io/docs/user-guide/install/rpi/).
5. [AWS SNS subscription](https://aws.amazon.com/sns/).


## Installation and Configuration:

1. Install Pareto Anywhere on Raspberry Pi. Follow the step-by-step instructions available [here](https://reelyactive.github.io/diy/pareto-anywhere-pi/).
   Pareto Anywhere is an IoT middleware that makes extracting data from BLE devices much easier, and it can be installed on local, cloud, and Edge devices.
   
   ![alt_text](https://github.com/withabubaker/Environment-Tracker/blob/main/IMG/ParetoAnywhereScreen.jpg)
   
2. Install ThingsBoard on Raspberry Pi. Step-by-step instructions available [here](https://thingsboard.io/docs/user-guide/install/rpi/)

3. Setup Minew S1 BLE Sensor [here](https://reelyactive.github.io/diy/minew-s1-config/)


<a href="https://www.youtube.com/watch?v=R392Zyts5yM">
  <img src="https://img.youtube.com/vi/R392Zyts5yM/maxresdefault.jpg" alt="Watch the video" width="500"/>
