# _*_ coding: utf-8 _*_
import threading
import time

# 定义某个线程要运行的函数


def countNum():
    global num
    num += 2
    print('running on number: %s \r' %num)
    time.sleep(1)

num = 1000000

if __name__ == '__main__':
    # 生成线程
    t1 = threading.Thread(target=countNum)
    t2 = threading.Thread(target=countNum)

    # 启动线程
    # t1.setDaemon(True)
    # t2.setDaemon(True)
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('ending')