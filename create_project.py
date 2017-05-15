# coding: utf-8
# author: NJB
# email: mincau@163.com
# Copyright (c) 2017 Strack
import create_connect


def create_project(name):
    st = create_connect.connect()
    prj = st.project.create(data={"p_name": name,  "temp_id": 1})
    print prj
    return prj


def find_project(name, st):
    return st.project.find(filters="name={0}".format(name))


def upload_project_preview(prj, path, st):
    return st.project.upload(entity_id=int(prj.get("id")), path=path)


