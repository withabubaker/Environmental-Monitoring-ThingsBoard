# Real-Time Environmental Monitoring with BLE Sensors and MQTT
An inexpensive and efficient way to stream temperature and humidity data in real-time. This project uses open-source Pareto Anywhere middleware to fetch data from Minew S1 BLE sensor, then pushes the readings to a ThingsBoard dashboard via the MQTT protocol. It also supports sending alerts via AWS SNS based on temperature or humidity thresholds, making it ideal for smart buildings, labs, or manufacturing environments. 

## Project Goals:

- Use Pareto Anywhere to capture temperature and humidity data from the Minew S1 BLE Sensor.
- Send the data to ThingsBoard via the MQTT protocol.
- Display the data on the ThingsBoard dashboard.
- Send SMS notifications via AWS SNS based on temperature or humidity thresholds.
