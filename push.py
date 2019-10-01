# -*- coding: utf-8 -*-
import json
import requests
import config

headers = {
    'Content-Type': 'application/json',
}


def msg(job_id, title, url, cache):
    _msg = {
        'job_id': job_id,
        'cards': [
            {
                'images': [],
                'title': title,
                'text': '更新了',
                'url': url
            },

        ],
        'cache': cache
    }
    data = json.dumps(_msg)
    response = requests.post(url=config.PUSH_MSG_URL, headers=headers, data=data)
    print('server response:{}\npush msg done.\n'.format(response.text))
