import time

status = 0

while status < 5:
    print("Checking server status...")
    time.sleep(2)  
    status = status + 1  
