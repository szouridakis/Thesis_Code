# Thesis_Code

## Title: Development of a system for simultaneous recording of multiple bio-signals in a non invasive way

This project code was developed as part of my Thesis for MEng in Electrical and Computer Engineering at Technical University of Crete in close collaboration with the Foundation of Research and Technology (FORTH) in Heraklion/Crete.

**Serial_Data folder** contains the Arduino code needed to receive data from all the following sensors:

- Adafruit AMG8833 8x8 Thermal Camera
- Adafruit MCP9808 Precision I2C Temperature
- Melexis MLX90614 IR Thermometer 
- DHT22/AM2302 Humidity Sensor 
- SparkFun Soil Moisture Sensor

**datastream11.py:** contains logic to receive information from the Arduino and save it to hdf5 files periodically.

**ui.py:** displays the measurements in screen in real time

**data_handling folder:** contains 2 files to retrieve the saved data from hdf5 files and create plots with them for the needs of the project

You can find the full report of the Thesis (in Greek) in this link:
https://dias.library.tuc.gr/view/87304