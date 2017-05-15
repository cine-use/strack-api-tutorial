# coding=utf8
# Copyright (c) 2017 Strack
import create_connect
st = create_connect.connect()
prj_name = "tes11"
epi_name = "01_island"
project = st.project.find(filters="name={0}".format(prj_name))
epi = st.episode.find(filters="name={0} and project_id={1}".format(epi_name, project.get("id")))
print epi
print project
seq_name = '01_meet_franck'
print st.sequence.find(filters="name={0} and project_id={1}".format(seq_name, project.get("id")))