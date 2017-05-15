# coding=utf8
# Copyright (c) 2017 Strack


def create_step(name, st):
    try:
        step = st.step.create(data={"name": name, "alias": name, "color": "9e9e9e"})
    except:
        step = st.step.find(filters="name={0}".format(name))
    return step


if __name__ == "__main__":
    from create_connect import *

    st = get_session(base_url, user, key)
    step = create_step("Rig1", st)
    print step
