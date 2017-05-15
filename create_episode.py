# coding=utf8
# Copyright (c) 2017 Strack


def create_episode(name, project, st):
    try:
        epi = st.episode.create(data={"name": name, "project_id": project.get("id")})
    except:
        epi = find_episode(name, project, st)
    return epi


def find_episode(name, project, st):
    return st.episode.find(filters="name={0} and project_id={1}".format(name, project.get("id")))


def upload_episode_preview(epi, path, st):
    return st.episode.upload(entity_id=int(epi.get("id")), path=path)