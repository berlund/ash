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
    

schedule.every(15).minutes.do(job)
schedule.every().day.at("08:00").do(job)
schedule.every().day.at("08:15").do(job)
schedule.every().day.at("08:30").do(job)
schedule.every().day.at("08:45").do(job)
schedule.every().day.at("09:00").do(job)

schedule.every().day.at("16:00").do(job)
schedule.every().day.at("16:15").do(job)
schedule.every().day.at("16:30").do(job)
schedule.every().day.at("16:45").do(job)
schedule.every().day.at("17:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)