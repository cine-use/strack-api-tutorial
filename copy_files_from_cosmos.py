# coding: utf-8
# author: NJB
# email: mincau@163.com
# Copyright (c) 2017 Strack
import os
root_dir = r"D:\BaiduNetdiskDownload\Cosmos Laundromat\Disc2\scenes"
dst_dir = r"D:\work\resource\cosmos"
for root, dirs, files in os.walk(root_dir):

    rel_path = root[len(root_dir)+1:]
    if not rel_path:
        rel_path = dst_dir
    else:
        rel_path = os.path.join(dst_dir, rel_path)

    for d in dirs:
        sub_dir = os.path.join(rel_path, d)
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)

    for f in files:
        f_path = os.path.join(rel_path, f)
        if os.path.exists(f_path):
            f = open(f_path, "w")
            f.write("")
            f.close()

print "copy files and dirs from 'cosmos laundromat' done!"
