from scrapy.cmdline import execute
import schedule
import time


def job():
    execute(['scrapy', 'crawl', 'ticket'])
    # , '--nolog'


if __name__ == '__main__':
    schedule.every().day.at("7:15").do(job_func=job)

    while True:
        schedule.run_pending()
        time.sleep(60)
