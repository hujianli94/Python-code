#!/usr/bin/env python
#-*- coding:utf8 -*-
import threading
import time
class myThreada(threading.Thread):
    def run(self):
        evt.wait()
        time.sleep(1)
        print(self.name,":Good morning!")
        evt.clear()
        time.sleep(2)
        evt.set()
        time.sleep(2)
        evt.wait()
        print(self.name,":I'm fine,thank you.")

class myThreadb(threading.Thread):
    def run(self):
        print(self.name,":Good moring!")
        evt.set()
        time.sleep(2)
        evt.wait()
        print(self.name,": How are you?")
        evt.clear()
        time.sleep(2)
        evt.set()

evt = threading.Event()
def main():
    John = myThreada()
    John.name = "John"
    Smith = myThreadb()
    Smith.name = 'Smith'
    John.start()
    Smith.start()

if __name__ == '__main__':
    main()