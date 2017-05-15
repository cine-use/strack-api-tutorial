# coding=utf8
# Copyright (c) 2017 Strack


def create_sequence(name, project, episode, st):
    try:
        seq = st.sequence.create(data={"name": name, "project_id": project.get("id"), "episode_id": episode.get("id")})
    except:
        seq = find_sequence(name, project, st)

    return seq


def find_sequence(name, project, st):
    return st.sequence.find(filters="name={0} and project_id={1}".format(name, project.get("id")))


def upload_sequence_preview(seq, path, st):
    return st.sequence.upload(entity_id=int(seq.get("id")), path=path)
