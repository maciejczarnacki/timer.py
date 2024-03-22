# A simple application showing how my timer works.

import timer as tm

import time

my_timer = tm.Timer(units='s', precision=0)

def main():
    print('Start')

    my_timer.start()

    time.sleep(7)

    print('Check, elapsed time: ', my_timer.check())

    time.sleep(7)

    print('Stop, elapsed time: ', my_timer.stop())


if __name__ == '__main__':
    main()


