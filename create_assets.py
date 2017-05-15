# coding: utf-8
# author: NJB
# email: mincau@163.com
# Copyright (c) 2017 Strack


def create_asset(name, category, project, st):
    try:
        asset = st.asset.create(data={"name": name, "project_id": project.get("id"), "category_id": category.get("id")})
    except:
        asset = find_asset(name, project, st)
    return asset


def find_asset(name, project, st):
    return st.asset.find(filters="name={0} and project_id={1}".format(name, project.get("id")))


def upload_asset_preview(asset, path, st):
    return st.shot.upload(entity_id=int(asset.get("id")), path=path)
