# coding: utf-8
# author: NJB
# email: mincau@163.com
# Copyright (c) 2017 Strack
import sys
sys.path.append(r"your strack api package path")
from strack_api.strack import Strack

base_url = "http://your strack web url"
user = "username"
key = "your api key"


def get_session(url, user, api_key):
    st = Strack(base_url=url,
                login=user,
                api_key=api_key)
    return st






