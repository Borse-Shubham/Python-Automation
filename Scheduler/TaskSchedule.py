import datetime
import schedule
import time

def Schedule_Minute():
    print("Schedular schedules after a minute...")
    print("current time is ",datetime.datetime.now())
    
    def Schedule_Hour():
    print("Schedular schedules after a Hour...")
    print("current time is ",datetime.datetime.now())

def main():
    print("Automations using pyhton")

    schedule.every(10).seconds.do(Schedule_Minute)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()