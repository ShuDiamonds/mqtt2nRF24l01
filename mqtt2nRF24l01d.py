#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
import os
import sys
import time

import mqtt2nRF24l01


def fork():
    pid = os.fork()

    if pid > 0:
        f = open('/var/run/mqtt2nRF24l01d.pid','w')
        f.write(str(pid)+"\n")
        f.close()
        sys.exit()

    if pid == 0:
        time.sleep(20)
        mqtt2nRF24l01.main()
        #print("a")
        




if __name__=='__main__': 
    fork()

