import os, sys, signal, time
from datetime import datetime

i = 0
total = raw_input("Enter number of tests : ")
latArray = []
dlArray = []
ulArray = []
timeArray = []

def printResults():
    latAvg = calcAverage(latArray)
    latMax = max(latArray)
    latMin = min(latArray)

    dlAvg = calcAverage(dlArray)
    dlMax = max(dlArray)
    dlMin = min(dlArray)

    ulAvg = calcAverage(ulArray)
    ulMax = max(ulArray)
    ulMin = min(ulArray)

    print("\n\nFrom {} to {}".format(timeArray[0], timeArray[-1]))
    print("\nLatency    |  Average: {:.2f} ms    |  Max: {:.2f} ms    |  Min: {:.2f} ms".format(latAvg, latMax, latMin))
    print("Download   |  Average: {:.2f} Mb/s  |  Max: {:.2f} Mb/s  |  Min: {:.2f} Mb/s".format(dlAvg, dlMax, dlMin))
    print("Upload     |  Average: {:.2f} Mb/s  |  Max: {:.2f} Mb/s  |  Min: {:.2f} Mb/s\n".format(ulAvg, ulMax, ulMin)) 



def calcAverage(nums):
    sum_nums = 0
    for i in nums:
        sum_nums += i
    avg = sum_nums / len(nums)
    return avg



while i < int(total):
 
    try:
        myCmd = 'speedtest > tests/testResult{}.txt'.format(i)
        
        now = datetime.now().time()
        timeArray.append(now)

        os.system(myCmd)
        
        testFile = open("tests/testResult{}.txt".format(i))

        lines = testFile.readlines()
        
        latency = lines[5]
        download = lines[6]
        upload = lines[7]

        latSplit = latency.split()
        latValue = float(latSplit[1])
        latArray.append(latValue)

        dlSplit = download.split()
        dlValue = float(dlSplit[1])
        dlArray.append(dlValue)

        ulSplit = upload.split()
        ulValue = float(ulSplit[1])
        ulArray.append(ulValue)

        print("Test #{} at {}  |  Latency: {:.2f} ms,    Download: {:.2f} Mb/s,    Upload: {:.2f} Mb/s".format(i + 1, now, latValue, dlValue, ulValue))
        i += 1
        time.sleep(25)
        
    except:
        printResults()
        exit()
    


