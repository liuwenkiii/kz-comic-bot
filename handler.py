# -*- coding: utf-8 -*-
import lxml.html
import requests
import push

etree = lxml.html.etree


def handle_job(jobs):
    print("handle job start.\n")
    for job in jobs:
        _handle(job)
    print("handle job done.\n")


def _handle(job):
    job_id = _get_job_id(job)
    link = _get_link(job)
    cache = _get_cache(job)
    response = requests.get(link)
    parse_result = _parse(response)
    if (len(cache) == 0) or (cache['latest_comic'] != parse_result['latest_comic']):
        title = parse_result['latest_comic']
        cache_ = {
           'latest_comic': parse_result['latest_comic']
        }
        url = "http://m.acg456.com" + parse_result['latest_comic_url']
        push.msg(job_id, title, url, cache_)
        print("push msg start.\n")
    else:
        print("already push.\n")


def _parse(response):
    selector = etree.HTML(response.text)
    latest_comic = selector.xpath('//*[@id="page"]/div[3]/ul/li[2]/div/a[1]/div/text()')[0]
    latest_comic_url = selector.xpath('//*[@id="page"]/div[3]/ul/li[2]/div/a[1]/@href')[0]
    print("latest: {}\nlatest_url: {}".format(latest_comic, latest_comic_url))
    return {'latest_comic': latest_comic, 'latest_comic_url': latest_comic_url}


def _get_job_id(job):
    job_id = job['job']['job_id']
    print("job_id: {}".format(job_id))
    return job_id


def _get_link(job):
    link = job['job']['params']['link']
    print("target link: {}".format(link))
    return link


def _get_cache(job):
    cache = job['cache']
    print("cache: {}".format(cache))
    return cache

