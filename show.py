import matplotlib.pyplot as plt
import numpy as np
import time
# 调用方法:实例化类后调用turn函数，在其后用time.sleep()延时
class Window: # 最后关闭窗口不可手动关闭，否则会弹出空白窗口并报错
    def __init__(self, max):
        # plt.ion()
        self.max = max
        self.fig = plt.figure()
        self.fig.patch.set_facecolor('black')
        self.ax = self.fig.add_subplot(111, projection='polar')
        self.ax.grid(True)
        self.ax.patch.set_facecolor("black")
        self.frame_theta = np.arange(0, 3.17, 0.1)
        self.frame_r = [max for i in range(len(self.frame_theta))]
        self.ax.plot(self.frame_theta, self.frame_r, linewidth=3, color='green')
    def recove(self):
        self.ax = self.fig.add_subplot(111, projection='polar')
        self.ax.grid(True)
        self.ax.patch.set_facecolor("black")
        self.ax.plot(self.frame_theta, self.frame_r, linewidth=3, color='green')
    def turn(self, theta, r): # 传入极角与极径(>0)
        # 由绘图速度所限刷新率最高为8Hz
        start = time.time()
        if r <= 0:
            r = 0.1
        r = np.arange(0, r, 0.1) # 起点 终点 步长
        theta = [theta]
        for i in range(len(r) - 1):
            theta.append(theta[0])
        self.recove()
        plt.ion()
        self.ax.plot(theta, r, linewidth = 3,color = 'green')
        plt.pause(0.0000001)
        # print(time.time() - start)
        plt.clf()
        plt.ioff()
if __name__ == '__main__':
    win = Window(50)
    step = 4
    while 1:
        for i in range(0, 314, step):
            start = time.time()
            win.turn(i / 100, 50)
            while time.time() - start <= 1 / 8:
                print(1)
                pass
        for i in range(0, 314, step):
            start = time.time()
            win.turn((314 - i) / 100, 50)
            while time.time() - start <= 1 / 8:
                print(1)
                pass