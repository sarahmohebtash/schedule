import time
import datetime
import schedule


def reminder():
    with open('file1.txt', "w") as file:
        file.write("remindddd!!!!")

schedule.every().day.at("09:00").do(reminder)

while True:
    schedule.run_pending()
    time.sleep(1)


def every():
    return None
