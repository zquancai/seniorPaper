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

Created on 2013-5-26

@author: Chine
'''

import re

from cola.core.errors import ConfigurationError
from cola.job.context import Context

JOB_NAME_RE = re.compile(r'(\w| )+')

class Job(object):
    def __init__(self, name, url_patterns, opener_cls, starts,
                 is_bundle=False, unit_cls=str,
                 instances=1, debug=False, user_conf=None,
                 login_hook=None):
        self.name = name
        self.real_name = self.name.replace(' ', '_')
        
        if not JOB_NAME_RE.match(name):
            raise ConfigurationError('Job name can only contain alphabet, number and space.')
        self.url_patterns = url_patterns
        self.opener_cls = opener_cls
        self.starts = starts
        
        self.is_bundle = is_bundle
        self.unit_cls = unit_cls
        self.instances = instances
        self.debug = debug
        self.user_conf = user_conf
        self.login_hook = login_hook
        
        self.context = Context(user_conf=user_conf)
        
    def add_urlpattern(self, url_pattern):
        self.url_patterns += url_pattern
        
    def set_userconf(self, conf):
        self.user_conf = conf
        self.context = Context(user_conf=self.user_conf)