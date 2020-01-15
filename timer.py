import schedule
import time
import screenshot
import functools

def job():
    try:
        screenshot.do()
    except:
        import traceback
        print(traceback.format_exc())
    

#7-8, 16-17
schedule.every(1).minute.do(job)
schedule.every().day.at("07:00").do(job)
schedule.every().day.at("07:15").do(job)
schedule.every().day.at("07:30").do(job)
schedule.every().day.at("07:45").do(job)
schedule.every().day.at("08:00").do(job)



schedule.every().day.at("16:00").do(job)
schedule.every().day.at("16:15").do(job)
schedule.every().day.at("16:30").do(job)
schedule.every().day.at("16:45").do(job)
schedule.every().day.at("17:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)