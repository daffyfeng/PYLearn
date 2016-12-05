#import sys
"""research how to write log"""
from datetime import datetime
import time

DATE_FMT = ""

#print sys.path

# dd
def readlog():
    """read log file"""
    file_open = open('text.txt', 'r')
    try:
        text_content = file_open.read()
    finally:
        file_open.close()
    return text_content

# writelog
def writelog(log):
    """write log file"""
    file_open = open('text.txt', 'a+')
    try:
        file_open.writelines(log + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")+'\r\n')
    finally:
        file_open.close()



if __name__ == '__main__':
    writelog('1. ')
    print readlog()
    time.sleep(20)
    writelog('2. ')
    print readlog()
