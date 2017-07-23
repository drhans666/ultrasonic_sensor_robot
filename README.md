# ultrasonic_sensor_robot
![Alt text](/measurement.jpg?raw=true "Measurement layer on photo")

Script have two parts:</br>
</br>
PART 1:</br>
radar.py, database.py, distance.py</br>
This part let you handle Your robot which should conatin of 5v, 180 degree servo engine and HC SR04 ultrasonic sensor.</br> You run it by opening radar.py. It takes measurements and save them to database.</br>
This files should be written on Your raspberry pi</br>
</br>
PART 2:</br> 
</br>
Second part consist of desktop.py which should be on your PC/Raspberry pi with desktop version of raspbian.</br> When You transfer your sensor database from raspberry pi to your PC(if youre working with raspbian headless) or You have desktop version of raspbian
this part processes raw database data to X, Y coordinates and visualises them with pyplot chart. Visualization need some final touch ;)</br>
</br>
I've added example database -robotbase.db</br>
