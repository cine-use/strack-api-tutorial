# coding=utf8
# Copyright (c) 2017 Strack
import os
from create_connect import *
from create_episode import *
from create_sequence import *
from create_shot import *
from create_step import *
from create_project import *
from create_task import *
from create_all_assets import create_all_assets


def create_episode_sequence_shot(project_name):
    # 过滤step用
    steps = ['sim', 'layout', 'anim', 'lighting', 'comp']

    # 保存创建的Episode，Sequence，Shot
    episodes = dict()
    sequences = dict()
    shots = dict()

    # 获取strack对象，供后续使用
    st = get_session(base_url, user, key)

    # 查找项目
    prj = find_project(project_name, st)

    # 遍历res/cosmos目录
    root_dir = os.path.join(os.path.dirname(__file__), "res/cosmos")
    for root, dirs, files in os.walk(root_dir):

        # 获取当前路径和res/cosmos的相对路径
        rel_dir = root[len(root_dir)+1:]
        rel_dir = rel_dir.split("\\")

        # 用/区分路径，根据list长度可判断是Episode, Sequcne,Shot
        if len(rel_dir) == 1:
            name = rel_dir[0]

            # res/cosmos目录就跳过
            if not name:
                continue

            epi = create_episode(name, prj, st)

            print epi
            episodes[name] = epi
            # 　手动放入的预览图片，就在目录下面，如果没有就不上传
            if files:
                f_path = os.path.join(root, files[0])
                upload_episode_preview(epi, f_path, st)

        elif len(rel_dir) == 2:
            e_name = rel_dir[0]
            s_name = rel_dir[1]
            seq = create_sequence(s_name, prj, episodes[e_name], st)

            sequences[s_name] = seq
            if files:
                f_path = os.path.join(root, files[0])
                upload_sequence_preview(seq, f_path, st)

            print seq

        elif len(rel_dir) == 3:
            s_name = rel_dir[1]
            t_name = rel_dir[2]
            shot = create_shot(t_name, prj, sequences[s_name], st)
            shots[t_name] = shot
            print shot
            for f in files:
                if ".png" in f:
                    full_path = os.path.join(root, f)
                    upload_shot_preview(shot, full_path, st)

                else:
                    names = f.split(".")
                    if len(names) > 2:
                        tep = names[1]

                        # 判断step，如果不在我们规定的里面就强制为lighting
                        for s in steps:
                            if s in tep:
                                tep = s
                        if tep not in steps:
                            tep = "lighting"
                        step = create_step(tep, st)
                        task = create_task(names[1], shot, step, prj, st)
                        print task


if __name__ == "__main__":
    prj_name = "cosmos3"
    create_episode_sequence_shot(prj_name)
