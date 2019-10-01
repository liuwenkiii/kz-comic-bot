# -*- coding: utf-8 -*-
import job
import handler
import time


def run():
    print("————————————————————")
    t = time.asctime(time.localtime(time.time()))
    print("date: {}\n".format(t))
    jobs = job.get_job()
    if len(jobs) > 0:
        handler.handle_job(jobs)
    else:
        print("no job.")
    print("————————————————————")


if __name__ == '__main__':
    run()
