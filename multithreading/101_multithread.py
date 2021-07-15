'''
python multithreading
create sub-thread

create
start()
'''

import logging
import threading
import time


def thread_func(num):
    logging.info('sub-thread is started.')

    time.sleep(3)
    for i in range(num):
        logging.info('in sub thread - %d', i)

    logging.info('sub-thread is end.')


if __name__=='__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("In the Main thread")

    new_thread = threading.Thread(target=thread_func, args=(100,))
    new_thread.start()

    logging.info('main thread end.')
