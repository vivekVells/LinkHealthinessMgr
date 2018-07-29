#! /usr/bin/python

###############################################################################
# navlinkverify.py - program to verify given link's reliability#
###############################################################################

import time
import requests

# read urls from file
def readFile():
    with open("testurllilnks.txt", "r") as file:
        urls = file.read().splitlines()

    verifyUrls(urls)

# verify urls healthiness
def verifyUrls(urls):
    print("Testing urls on " + time.ctime() + "\n")

    for url in urls:
        try:
            r = requests.get((url), timeout=5)
            print(str(r.status_code) + '\t' + url)
        except requests.exceptions.ConnectionError:
            print("connection error...")

# main function that runs when this program starts
def main():
    readFile()

# which function to run controller
if __name__ == '__main__':
    main()

"""
Output:
C:\Developer\Python36\python.exe E:/kevDev/ProjectWorks/LinkHealthinessMgr/linkhealthinessmgr/navlinkverify.py
Testing urls on Sat Jul 28 20:14:37 2018

200	http://google.com
200	http://www.linkedin.com
404	https://www.express-scripts.com/trghn
............................................
"""