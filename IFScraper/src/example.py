#!/usr/bin/python

import os
import sys
import threading
import time
from Queue import Queue
from random import randint

def fetchURL(index):
    sleep_time = randint(1,5)
    print("Index %i, sleeping for %i...")%(index,sleep_time)
    time.sleep(sleep_time)

    return()

def process_queue(q):
    
    while not q.empty():
    
        work = q.get()
        fetchURL(work)
        
        q.task_done()
    return True
    

def main():

    main_queue = Queue(maxsize=0)
    

    urlList = range(1,1001)
    
    num_threads = min(500, len(urlList))
    
    for url in urlList:
        main_queue.put(url)
    
    for i in range(num_threads):
        print("Starting thread")
        worker = threading.Thread(target=process_queue, args=(main_queue,))
        worker.setDaemon(True)
        worker.start()
    
    main_queue.join()
        
        
        # increment available thread list
        
    print("Completed the URL list")
            
    
    
    #fetchURL()
        
    return()


main()
