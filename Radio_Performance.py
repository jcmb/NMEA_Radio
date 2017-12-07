#!/usr/bin/env python
from __future__ import division

import sys

try:
  import pynmea2  
except:
  sys.exit("ERROR: pynmea2 module not installed, install using pip install pynmea2")
  
import socket
from pprint import pprint
from collections import defaultdict
import argparse

from datetime import datetime,date,timedelta

def Perform_Test(TCP_IP,TCP_PORT,Test_Time,VERBOSE):
  Testing=True
  Started_Test=False
  RTK_Epochs=0
  Non_RTK_Epochs=0
  BUFFER_SIZE = 1024
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  print TCP_IP
#  print TCP_PORT
#  print s
  s.connect((TCP_IP, TCP_PORT))
  Ages=defaultdict(int)

  #Ages[5]=1

  while Testing:
    data = s.recv(BUFFER_SIZE)
    data=data.rstrip()
    if VERBOSE:
      print "received data:",data

    try:
      msg = pynmea2.parse(data)
    except:
      sys.stderr.write("Parse Error: {}\n".format(data))
      continue
   
#    print msg 
    if msg.gps_qual==0:
      sys.exit("GNSS Reciever must be positioning")
      
    NMEA_datetime=datetime.combine(date.today(),msg.timestamp)
    
    if Started_Test == False:
      Started_Test=msg.timestamp.second==0 or True
      if Started_Test:
        Start_Time=NMEA_datetime
        End_Time=NMEA_datetime+timedelta(seconds=Test_Time)
        if VERBOSE:
          sys.stderr.write("Test Started at: {}\n".format(msg.timestamp))
          sys.stderr.write("Test to end at: {}\n".format(End_Time))

    if Started_Test :
      if NMEA_datetime>= End_Time:
        Testing=False
        if VERBOSE:
          sys.stderr.write("Finished\n")
        continue
      
    if msg.gps_qual==1 or msg.gps_qual==2:
      Non_RTK_Epochs+=1

    if msg.gps_qual==4 or msg.gps_qual==5:
      RTK_Epochs+=1
      age=int(float(msg.age_gps_data))
      Ages[age]+=1

  #  pprint (msg)
  s.close()
    
  return (Non_RTK_Epochs,RTK_Epochs,Start_Time,End_Time,Ages)
  
def Report_Test_CSV(HOST,PORT,Test_NAME,Test_Time,Start_Time,End_Time,Non_RTK_Epochs,RTK_Epochs,Ages):
  result="\"{}\",{},\"{}\",{},{},{},{},{}".format(HOST,PORT,Test_NAME,Start_Time,End_Time,Test_Time,RTK_Epochs,Non_RTK_Epochs)
  age_str=""
  if RTK_Epochs <> 0:
    max_age = max(Ages.keys())
    current_age=1

    while current_age<=max_age:
      age_str+=",{},{}%".format(Ages[current_age],Ages[current_age]/RTK_Epochs*100)
      current_age+=1
  result+=age_str
  sys.stdout.write("{}\n".format(result))
  
def Report_Test(HOST,PORT,Test_NAME,Test_Time,Start_Time,End_Time,Non_RTK_Epochs,RTK_Epochs,Ages):
  if Test_NAME <> "":
    print Test_NAME
  print "RTK: {} ({}%) Non RTK: {} ({}%)".format(RTK_Epochs,RTK_Epochs/Test_Time*100,Non_RTK_Epochs,Non_RTK_Epochs/Test_Time*100)
  if RTK_Epochs <> 0:
    max_age = max(Ages.keys())
    current_age=1

    while current_age<=max_age:
      print "{}: {} ({}%)".format(current_age,Ages[current_age],Ages[current_age]/RTK_Epochs*100)
      current_age+=1

def create_arg_parser():
    usage="Radio_Performance.py <Host> <Port> [Test Name]"
    parser=argparse.ArgumentParser(prog="Radio_Performance.py")
    parser.add_argument('--version', action='version', version='%(prog)s 0.8')
    parser.add_argument("host", type=str, help="GNSS Receiver IP")
    parser.add_argument("port", type=int, help="GNSS Port")
    parser.add_argument("name",type=str,nargs="*", default="",help="Test Name")
    parser.add_argument("-T", "--tell",action="store_true", dest="tell", default=False, help="Tell the settings for the run")
    parser.add_argument("-c", "--csv",action="store_true", dest="csv", default=False, help="Output in a CSV Format")
    parser.add_argument("-d", "--duration",type=int, default=100, help="Test Time, in seconds")
    parser.add_argument('-v', '--verbose', action='count', default=0,
                   help='increase output verbosity (use up to 3 times)')

    return (parser)

def process_arguments ():
    parser=create_arg_parser()
    options = parser.parse_args()
#    print options
    VERBOSE=options.verbose
    if options.name ==[]:
      NAME=""
    else:
      NAME=" ".join(options.name)
    HOST=options.host
    PORT=options.port
    CSV=options.csv
    DURATION=options.duration
    if NAME==None:
      NAME=""

    if options.tell:
        sys.stderr.write("Host: " + HOST+ "\n")
        sys.stderr.write("Port: " +  str(PORT)+ "\n")
        sys.stderr.write("Test Time: " + str(DURATION)+ "\n")
        sys.stderr.write("Test Name: " + str(NAME)+ "\n")
        sys.stderr.write("CSV Format: " + str(CSV)      + "\n")
        sys.stderr.write("Verbose: " + str(VERBOSE)  + "\n")
    
    return (HOST,PORT,DURATION,NAME,CSV,VERBOSE)

def main():

  (HOST,PORT,Test_Time,Test_NAME,CSV,VERBOSE)=process_arguments()
  (Non_RTK_Epochs,RTK_Epochs,Start_Time,End_Time,Ages)=Perform_Test(HOST,PORT,Test_Time,VERBOSE)  
  if CSV:
    Report_Test_CSV(HOST,PORT,Test_NAME,Test_Time,Start_Time,End_Time,Non_RTK_Epochs,RTK_Epochs,Ages)
  else:
    Report_Test(HOST,PORT,Test_NAME,Test_Time,Start_Time,End_Time,Non_RTK_Epochs,RTK_Epochs,Ages)

main()


