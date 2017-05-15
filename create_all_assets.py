# coding=utf8
# Copyright (c) 2017 Strack
import os
import re
import glob
from create_connect import *
from create_project import find_project
from create_assets import create_asset,upload_asset_preview
from create_task import create_task
from create_step import create_step

CATEGORY_MAP = {
    "props": "Prop",
    "chars": "Character",
    "envs": "Environment"
}
STEP_MAP = {
    "rig" : "Rig",
    "shading" : "Surface",
    "anim": "anim",
    "layout": "layout",
    "poses":"poses",
    "sculpt": "sculpt",
    "shapes": "shapes",
    "simulation": "simulation"
}


def parse_path(file_path):
    path = os.path.dirname(file_path)
    file = os.path.basename(file_path)
    new_filename = file.replace('.blend', '.png')
    path = os.path.join(path, new_filename)
    fields = re.split(r'[\/\\]+', file_path)
    if len(fields) == 8:
        _, _, _, _, _, category, asset_name, file_name = fields
    elif len(fields) == 9:
        _, _, _, _, _, category, _othersheep, asset_name, file_name = fields
    else:
        return
    fields = file_name.split(".")
    if len(fields) == 3:
        step = fields[1]
    else:
        step = None
    return {
            "category": category,
            "asset_name": asset_name,
            "file_name": file_name,
            "step": step,
            "path": path
            }


def create_all_assets(project_name="Cosmos Laundromat"):
    # get st object
    st = get_session(base_url, user, key)
    # get project
    project = find_project(project_name, st)
    # get file path
    root_dir = os.path.join(os.path.dirname(__file__), r"res/assets")
    file_dir = os.path.normpath(root_dir + r'\*\*\*.blend')
    file_list = glob.iglob(file_dir)
    # parse data
    data_list = map(parse_path, file_list)
    # create assets from data
    new_assets = []
    new_tasks = []
    for i in data_list:
        asset_name = i["asset_name"]
        if not asset_name:
            continue
        category_name = CATEGORY_MAP.get(i["category"], "")
        category = st.category.find("name=%s" % category_name)
        if not category:
            continue
        step_name = STEP_MAP.get(i["step"], 'Rig')
        print step_name
        step = create_step(step_name, st)
        print step
        asset = create_asset(asset_name, category, project, st)
        task = create_task(asset_name, asset, step, project, st)
        new_assets.append(asset)
        new_tasks.append(task)
        path = i["path"]
        if os.path.isfile(path):
            upload_asset_preview(asset, path, st)
    # return new_assets
    return new_tasks


if __name__ == '__main__':
    print create_all_assets("cosmos3")





