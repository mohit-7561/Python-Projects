import time
from plyer import notification
if __name__ =="__main__":
    while True:
        notification.notify(
            title = "***Please Drink Water Now!***",
            message = "Hey Mohit! Wake up don't be too lazy to drink water as you are in the phase of creatine",
            app_icon = "C:\Python Notes\Python Projects\WaterNotification\icon.ico",
            timeout = 3
    )
        time.sleep(5)

        #pwd in terminal is used to find the path 
        #pythonw.exe in terminal is used to run the program in background