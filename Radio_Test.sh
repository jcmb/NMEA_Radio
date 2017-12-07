TEST_TIME=200
TEST_PORT=28001
CSV=--csv
./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.2 $TEST_PORT BTS-Base $@>>Results.csv&
./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.223 $TEST_PORT R15-SNB-254 $@>>Results.csv&
#./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.226 $TEST_PORT SPS986 $@>>Results.csv&
./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.228 $TEST_PORT SPS985 $@>>Results.csv&
./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.229 $TEST_PORT R12-532 $@>>Results.csv&
./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.230 $TEST_PORT R13-512 $@>>Results.csv&
./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.232 $TEST_PORT R10 $@>>Results.csv&
./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.31 $TEST_PORT R1-SNB-260 $@>>Results.csv&
./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.32 $TEST_PORT R2-482 $@>>Results.csv&
./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.34 $TEST_PORT R4-487 $@>>Results.csv&
./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.35 $TEST_PORT R5-SNB-261 $@>>Results.csv&
./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.51 $TEST_PORT Middle-470 $@>>Results.csv&
./Radio_Performance.py $CSV -T -d $TEST_TIME  192.168.128.65 $TEST_PORT R16-484 $@>>Results.csv&
