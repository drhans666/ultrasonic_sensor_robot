# ultrasonic_sensor_robot
Script has two parts:

PART 1:
radar.py, database.py, distance.py
This part let you handle Your robot which should conatin of 5v, 180 degree servo engine and HC SR04 ultrasonic sensor. You run it by opening radar.py. It takes measurements and save them to database.
This files should be written on Your raspberry pi

PART 2: 

Second part consist of desktop.py which should be on your PC/Raspberry pi with desktop version of raspbian. When You transfer your sensor database from raspberry pi to your PC(if youre working with raspbian headless) or You have desktop version of raspbian
this part processes raw database data to X, Y coordinates and visualises them with pyplot chart. Visualization need some final touch ;)

I've added example database -robotbase.db
