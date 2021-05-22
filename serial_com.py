import serial
import show
portx = "COM3"
bps = 9600
timex = 5
ser = serial.Serial(portx, bps, timeout=timex)
step = 4
win = show.Window(10)
while 1:
    try:
        theta = float(ser.readline().decode('UTF-8').replace("\n", "").replace("\r", ""))
    except UnicodeDecodeError or ValueError:
        theta = 0.0 # 单片机串口首次发来的字符为乱码，此方法虽不治本但是暂时没有问题
    r = float(ser.readline().decode('UTF-8').replace("\n", "").replace("\r", ""))
    win.turn(theta, r)
    print(theta, r)
ser.close()#关闭串口