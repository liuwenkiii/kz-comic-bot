# -*- coding: utf-8 -*-
import os
import config
import requests

JOB_FILE_PATH = os.path.join(os.getcwd(), 'jobs')
JOB_ID_LIST = []
JOB_LIST = []


def get_job():
    _update_job()
    return JOB_LIST


def _update_job():
    print("update job start.")
    JOB_ID_LIST.clear()
    JOB_LIST.clear()
    has_new_job = True
    while has_new_job:
        data = requests.get(config.GET_JOB_URL).json()
        errno = data['errno']
        errmsg = data['errmsg']
        if errno == 0:
            job_id = data['job']['job_id']
            has_new_job = _is_new_job(job_id)
            if has_new_job:
                JOB_ID_LIST.append(job_id)
                JOB_LIST.append(data)
                print("JOB_ID: {}".format(job_id))
        elif errno == 1:
            has_new_job = False
        else:
            print("errno: {}, errmsg: {}".format(errno, errmsg))
    print("update job done.\n")


def _is_new_job(job_id):
    for _id in JOB_ID_LIST:
        if _id == job_id:
            return False
    return True
