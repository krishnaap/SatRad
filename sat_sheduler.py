#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 00:10:04 2020

@author: krishna
"""

from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import time

def some_job():
    timestr = time.strftime("%Y%m%d-%H%M%S")                            # setting up time as a variable to use in filename.
    print ("Saving file @")                                             # Displaying the saving 
    print(timestr)                                                      #..
    image_url = "https://mausam.imd.gov.in/Satellite/3Dasiasec_ir1.jpg" 
    r = requests.get(image_url)                                         # create HTTP response object 
    filename = "%s.jpg" % timestr                                       # send a HTTP request to the server and save 
    with open(filename,'wb') as f: 
        f.write(r.content)                                              # the HTTP response in a response object called r                    
                                                                        # Saving received content as a png file in 
                                                                        # binary format 
                                                                        # write the contents of the response (r.content)
                                                                        # to a new file in binary mode.
                                                                 
scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes=20)                     # scheduler.add_job(some_job, 'interval', hours=1) as per 
scheduler.start()
