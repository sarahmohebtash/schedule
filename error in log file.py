import time

import schedule


def check_log_file():
    with open('log.txt', mode='r') as logfile:
           content = logfile.read()
    if "ERROR" in content:
            print("error found")

def review_schedule():
 schedule.every().hour.do(check_log_file)

review_schedule()

while True:
    schedule.run_pending()
    time.sleep(1)
