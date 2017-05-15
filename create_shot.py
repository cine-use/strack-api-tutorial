# coding: utf-8
# author: NJB
# email: mincau@163.com
# Copyright (c) 2017 Strack


def create_shot(name, project, sequence, st):
    try:
        shot = st.shot.create(data={"name": name, "project_id": project.get("id"), "sequence_id": sequence.get("id")})
    except:
        shot = find_shot(name, project, st)
    return shot


def find_shot(name, project, st):
    return st.shot.find(filters="name={0} and project_id={1}".format(name, project.get("id")))


def upload_shot_preview(shot, path, st):
    return st.shot.upload(entity_id=int(shot.get("id")), path=path)








