# coding: utf-8
# author: NJB
# email: mincau@163.com
# Copyright (c) 2017 Strack
import create_connect


def find_user(name):
    st = create_connect.connect()
    # prj = st.project.create(data={"p_name": name, "status_id": 10, "temp_id": 1})
    # user = st.user.create(data={"login": name})
    # print st.user.fields
    user = st.user.find(filters="login=niu")
    print user

find_user("test345")
