#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0

import os
from gps import *
from time import *
import time
import threading
import datetime
today = datetime.date.today()
todaystr = today.isoformat()

gpsd = None #seting the global variable

os.system('clear') #clear the terminal (optional)

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer


if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while gpsd.fix.latitude == 0.0:
      time.sleep(1)
    else:
      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc

      os.system('clear')
      time.sleep(0)
      file = open(todaystr + "/GPS_" + '{:%d.%m.%Y_%H:%M:%S}'.format(datetime.datetime.now()) + ".txt", "w+")
      file.write("GPS-Daten Raspinguin (ISE) vom " + '{:%d.%m.%Y_%H:%M:%S}'.format(datetime.datetime.now()))
      file.write("\n---------------------------------------------------")
      file.write("\nlatitude       " +  str(gpsd.fix.latitude))
      file.write("\nlongitude      " +  str(gpsd.fix.longitude))
      file.write("\ntime utc       " +  str(gpsd.utc))
      file.write("\naltitude (m)   " +  str(gpsd.fix.altitude))
      file.write("\neps            " +  str(gpsd.fix.eps))
      file.write("\nepx            " +  str(gpsd.fix.epx))
      file.write("\nept            " +  str(gpsd.fix.ept))
      file.write("\nspeed (m/s)    " +  str(gpsd.fix.speed))
      file.write("\nclimb          " +  str(gpsd.fix.climb))
      file.write("\ntrack          " +  str(gpsd.fix.track))
      file.write("\nmode           " +  str(gpsd.fix.mode))
      file.write("\n\nLog Datei wurde gesichert.")
      file.close()
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing

