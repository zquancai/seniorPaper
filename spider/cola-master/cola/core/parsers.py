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

Created on 2013-5-21

@author: Chine
'''

class Parser(object):
    def __init__(self, opener=None, url=None, **kwargs):
        self.opener = opener
        if url is not None:
            self.url = url
            
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
        
    def parse(self, url=None):
        raise NotImplementedError