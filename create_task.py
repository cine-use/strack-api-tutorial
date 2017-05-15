# coding=utf8
# Copyright (c) 2017 Strack


def create_task(name, shot, step, project, st):
    failed = False
    i = 1
    temp = name
    while not failed:
        try:
            task = st.task.create(data={"name": temp,
                                    "item_id": shot.get("id"),
                                    "step_id": step.get("id"),
                                    "project_id": project.get("id")})

            failed = True
        except Exception, e:
            print e
            temp = name + str(i)
            i += 1

    return task

if __name__ == "__main__":
    from create_connect import *
    from create_project import *
    from create_shot import *
    from create_sequence import *
    from create_step import *
    st = get_session(base_url, user, key)
    prj = find_project("tes11", st)
    seq = create_sequence("01_meet_franck", prj, None, st)
    shot = create_shot("01_01_01_A", prj, seq, st)
    step = create_step("render", st)
    task = st.task.create(data={"name": "abc2",
                                "item_id": shot.get("id"),
                                "step_id": step.get("id"),
                                "project_id": prj.get("id")})
    print task
