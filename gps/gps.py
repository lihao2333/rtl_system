import serial
def wait_time(time):
    with serial.Serial('/dev/ttyUSB0',9600) as ser:
        while True:
             datas = ser.readline().decode()
             datas = datas.strip("\r\n").split(",")
             if datas[0] == "$GNRMC":
                 hour = "%02d"%(int(datas[1][:2])+8)
                 minute = datas[1][2:4]
                 second = datas[1][4:6]
                 now = hour+minute+second
                 print(now)
                 if  time == now:
                     break
