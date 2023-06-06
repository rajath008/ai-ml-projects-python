from plyer import notification
import time

if __name__=='__main__':
    notification.notify(
        title="Title of the notification",
        message="This is the message of notification",
        # app_icon="D:/try.ico",
        timeout=5)
    time.sleep(10)


    
