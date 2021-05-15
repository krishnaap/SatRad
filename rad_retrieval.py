#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 00:10:04 2020

@author: krishna
"""

from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import time

# timestr = time.strftime("%Y%m%d-%H%M%S")

def some_job():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print ("Saving file @")
    print(timestr)
    image_url = "https://mausam.imd.gov.in/Radar/ppz_koc.gif"
    r = requests.get(image_url) # create HTTP response object 
    filename = "%s.gif" % timestr
    with open(filename,'wb') as f: 
        f.write(r.content)                                     # send a HTTP request to the server and save 
                                                               # the HTTP response in a response object called r 
                                                               # Saving received content as a png file in 
                                                               # binary format 
  
                                                                # write the contents of the response (r.content) 
                                                                 # to a new file in binary mode.
     
scheduler = BlockingScheduler()
# scheduler.add_job(some_job, 'interval', hours=1)
scheduler.add_job(some_job, 'interval', minutes=20)
scheduler.start()
