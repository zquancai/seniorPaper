#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (c) 2013 Qin Xuye <qin@qinxuye.me>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Created on 2013-6-22

@author: Chine
'''

import socket
import os

from cola.core.rpc import client_call
from cola.core.utils import get_ip
from cola.core.logs import get_logger
from cola.worker.recover import recover

from conf import user_config

logger = get_logger(name='sina_stop')

if __name__ == '__main__':
    ip, port = get_ip(), getattr(user_config.job, 'port')
    logger.info('Trying to stop single running worker')
    try:
        client_call('%s:%s' % (ip, port), 'stop')
    except socket.error:
        stop = raw_input("Force to stop? (y or n) ").strip()
        if stop == 'y' or stop == 'yes':
            job_path = os.path.split(os.path.abspath(__file__))[0]
            recover(job_path)
        else:
            print 'ignore'
    logger.info('Successfully stopped single running worker')
