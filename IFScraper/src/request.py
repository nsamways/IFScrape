### ImageFap Gallery Downloader
### request url content

import time
import threading
import config
import urllib2
import sys
import socket

def ReqUrl(urlstr):
    
    
    
    #if ((urlstr[:7] != "http://") and (urlstr[:8] != "https://" )): urlstr="http://"+urlstr
    
    #readTime = time.time()
    
    #dat = urllib2.urlopen(urlstr).read()
    
        
  
    
    #specify a timeout
    timeout = 10
    
    
    if ((urlstr[:7] != "http://") and (urlstr[:8] != "https://" )): urlstr="http://"+urlstr
    req = urllib2.Request(urlstr)
    ### spoof user-agent and try to appear as mozilla firefox
    req.add_header('User-Agent', config.useragent)
    opnr = urllib2.build_opener()
    ### Request contents of url
    #readTime = time.time()
    
    #specify a timeout
    timeout = 10
    socket.setdefaulttimeout(timeout)
    
    try:
        dat = opnr.open(req).read()
        # print("This is the DAT:")
        #print("Success:")
        #print("urlstr was: "+urlstr)
        #print(dat)
        # exit()
    except:
        dat = ""
        print("FAILED")
        #print("urlstr was: "+urlstr)
        #sys.exit()
    
    # print("was in request.py, reading for: " + str(round((time.time() - readTime),2))) 

    #print(dat)
    return dat

