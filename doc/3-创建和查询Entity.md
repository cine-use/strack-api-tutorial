### 创建和查询Entity

#### 1. 查询project
上一节已经创建了项目**test**， 现在需要获取此项目信息供后续使用。代码如下：
```
def find_project(name, st):
    return st.project.find(filters="name={0}".format(name))
```
需要传入项目名称，以及strack对象，上一节通过**get_session()**获取到的。


#### 2. 查询和创建Episode
```
    def create_episode(name, project, st):
        try:
            epi = st.episode.create(data={"name": name, "project_id": project.get("id")})
        except:
            epi = find_episode(name, project, st)
        return epi
```
为啥创建函数里面包着一个查找函数，这个说多了都是泪呀。平时写代码，难免产生错误，修改后
继续运行发现报错说重名，就得去Web上把对应的Episode删除掉，反反复复删来删去很烦。索性在
创建里面加入查询，创建不成，也能把已经创建的Episode给返回不影响后续代码运行。
查找函数如下：
```
    def find_episode(name, project, st):
        return st.episode.find(filters="name={0} and project_id={1}".format(
        name, project.get("id")))
```
上传缩略图
```
def upload_episode_preview(epi, path, st):
    return st.episode.upload(entity_id=int(epi.get("id")), path=path)
```
path是缩略图的完整路径。

Sequence，Shot，Asset和Episode的函数类似，只有参数不同，就不多说了，请参考
create_sequence.py， create_shot.py, create_task.py

#### 3. 创建Task
本教程就用到了创建Task，代码也很简单。
```
def create_task(name, shot, step, project, st):
    return st.task.create(data={"name": name,
                                "item_id": shot.get("id"),
                                "step_id": step.get("id"),
                                "project_id": project.get("id")})
```
就是传入的参数多了点，step要多说一下，是Task的环节或者工序，实际生产中有Model，Tex，Lighting
等。

#### 4. 获取Step
Step在系统中是全局存储的，获取参数更少，仅需要项目信息即可，代码如下：
```
def create_step(name, st):
    try:
        step = st.step.create(data={"name": name, "alias": name, "color": "9e9e9e"})
    except:
        step = st.step.find(filters="name={0}".format(name))
    return step
```