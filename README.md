#Radio_Performance.py

## A tool for monitoring radio performance using NMEA Messages

### Usage

>Radio_Performance.py [-h] [--version] [-T] [-c] [-d DURATION] [-v]
                            host port [name [name ...]]

####positional arguments:

>  host:                 GNSS Receiver IP or name

>  port:                 GNSS TCP Port that the NMEA GGA Messages are available on

>  name:                 Test Name


####optional arguments:

>-h, --help            

>      show this help message and exit

>--version             

>      show program's version number and exit

>-T, --tell            

>      Tell the settings for the run

>-c, --csv             

>      Output in a CSV Format

>-d DURATION, --duration DURATION

>      Test Time, in seconds

>-v, --verbose         

>      increase output verbosity (use up to 3 times)
  
### Usage Details


* Duration:

   The length of the time the test wil run for
   
* CSV:

   Output the information in CSV Format
      
* Tell:

   Report the arguments that are in use   
  
  
### CSV Format

The CSV Format has a fixed number of standard columns followed by details 

1. Host
2. Port
3. Test Name, with ""
4. Start Time of Test
5. End Time of Test
6. Test Time
7. RTK Epochs
8. Non RTK Epochs
9. Packet Received this epoch
10. Packet Received this epoch, %
11. Packet Received this epoch
12. Packet missed for 1 epoch
13. Packet missed for 1 epoch, %

Next Columns are repeating, 2 second, 3 second etc....
 
1. Number of Epochs of this age
2. % of Total Epochs of this age

## Requirements

pynmea2 

>*pip install pynmea2*
  
