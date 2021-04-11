import datetime
from datetime import timedelta
import threading
import time

 
now = datetime.datetime.now()
#the time is UTC
breakfast_time = datetime.datetime(2021, 4, 12, 13, 00, 00) 
delay = (breakfast_time - now).total_seconds()
def breakfast():
  engine.say("it is breakfast time")
  engine.runAndWait()
  time.sleep(60*60*24)
  breakfast()

threading.Timer(delay, breakfast).start()

lunch_time = datetime.datetime(2021, 4, 12, 18, 00, 00)
delay_lunch = (lunch_time - now).total_seconds()
def lunch():
  engine.say("it is lunch time")
  engine.runAndWait()
  time.sleep(60*60*24)
  lunch()

threading.Timer(delay, lunch).start()

dinner_time = datetime.datetime(2021, 4, 12, 22, 00, 00)
delay_dinner = (dinner_time - now).total_seconds()
def dinner():
  engine.say("it is dinner time")
  engine.runAndWait()
  time.sleep(60*60*24)
  dinner()

threading.Timer(delay, dinner).start()

