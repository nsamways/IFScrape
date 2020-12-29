#!/usr/bin/python


# -*- coding: utf-8 -*-

### ImageFap Gallery Downloader 0.4
### main module
### Working with Python 2.7; not tested with other versions

import config
import urlqueue
import gallery
import time
import sys

version = '0.4'

def main():
    print 'ImageFap Gallery Downloader '+version
    config.LoadConfig('IFLoad.config')
    print 'Ready\n'
   
    while True:
        ### fetch clipboard content and check for new url; add to queue if valid url is detected
        urlqueue.CheckClipboard()
        #print(urlqueue.CheckClipboard())    
        ### check if queue contains a url
        if len(urlqueue.queue): gallery.DownloadGallery()
            
        time.sleep(0.5)

main()
        
