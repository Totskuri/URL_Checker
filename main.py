import time
import datetime
import urllib.request
import urllib.error
import sys

websiteArray = []
contentArray = []
numOfWebsites = 0

def initiateArrays():
    #Initiating two arrays. One containing websites and another containing website content requirement.
    with open('conf.txt') as conf:
        for line in conf:
            if "http://" in line:
                line = line[:-1]
                websiteArray.append(line)
            else:
                line = line[:-1]
                contentArray.append(line)

def request(count):
    #Url request, time measure and content check
    try:
        startTime = time.time()
        url =  websiteArray[count]
        response = urllib.request.urlopen(url)
        html = response.read()
        htmlStr = str(html)
    except:
        writeLog(websiteArray[count], "Connection error", 0)
    else:
        totalTime = time.time() - startTime
        if contentArray[count] in str(htmlStr):
            writeLog(websiteArray[count], "Content ok", totalTime)
        else:
            writeLog(websiteArray[count], "Content error", totalTime)

def writeLog(url,logStr, totalTime):
    #Writing website info into log file
    with open("log.txt", 'a') as out:
        now = datetime.datetime.now()
        totalTime = totalTime * 1000
        timeStr = str(totalTime)
        strSep = '.'
        strRest = timeStr.split(strSep, 1)[0]
        out.write(str(now.day) + '.' + str(now.month) + '.' + str(now.year) + ' \t '
                  + str(now.hour) +':' + str(now.minute) + ':' + str(now.second) +
                  ' \t ' + url + ' \t ' + logStr + ' \t Ping: ' + strRest + ' ms\n')

if __name__=="__main__":
    #main loop
    initiateArrays()
    numOfWebsites = len(websiteArray)
    sleepTime = round(float(sys.argv[1]))

    count = 0
    while True:
        request(count)
        if count == numOfWebsites - 1:
            count = 0
            time.sleep(sleepTime)
        else:
            count += 1

