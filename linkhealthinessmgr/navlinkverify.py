#! /usr/bin/python

###############################################################################
# navlinkverify.py - program to verify given link's reliability#
###############################################################################

import time
import requests

# urls to be tested will be sent here
urlsToTest= [
    'http://google.com'
    ,'http://www.linkedin.com'
    ,'https://www.express-scripts.com/trghn'
]

# main function that runs when this program starts
def main():
    print("\nTesting started on...", time.ctime())

    for url in urlsToTest:
        try:
            r = requests.get(url, timeout=10)
            print(str(r.status_code) + '\t' + url)
        except requests.exceptions.ConnectionError:
            print("connection error...")

# which function to run controller
if __name__ == '__main__':
    main()

"""
Output:

C:\Developer\Python36\python.exe E:/kevDev/ProjectWorks/LinkHealthinessMgr/linkhealthinessmgr/navlinkverify.py

Testing started on... Sat Jul 28 16:57:52 2018
200	http://google.com
200	http://www.linkedin.com
404	https://www.express-scripts.com/trghn

Process finished with exit code 0
"""