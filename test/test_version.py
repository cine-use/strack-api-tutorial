# coding=utf8
# Copyright (c) 2017 Strack
import create_connect
from create_connect import *

# def find_user(name):
#     st = create_connect.connect()
#     # prj = st.project.create(data={"p_name": name, "status_id": 10, "temp_id": 1})
#     # user = st.user.create(data={"login": name})
#     # print st.user.fields
#     user = st.user.find(filters="login=niu")
#     print user


def create_version():
    st = get_session(base_url, user, key)
    # ver = st.version.create(data={"task_id": 38})
    # print ver
    v3 = st.version.select(filters="task_id=38 and version in 1,3,4,5 ")
    print v3
    # task = st.task.find(filters="")

create_version()
