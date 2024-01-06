from json import loads, dumps
from os.path import exists
from os import mkdir
from .logger import lyLogger

class Quester():
    # 获得 Logger 操作器
    logger = lyLogger('log/', 'server.log', 'Quester')
    json_file_path = './data/quest/list.json'
    def __init__(self):
        _Helper.checkDir()
        _Helper.checkFile(self.json_file_path)
    #
    # Start: Get #
    def getSimple(self):
        try:
            List = _Helper.getList(self.json_file_path)
            self.logger.log('获取全部数据 | 成功')
            return List
        except:
            self.logger.warn('获取全部数据 | 未找到文件')
            return []
    def getMain(self, target):
        try:
            List = _Helper.getList(self.json_file_path)
            for i in range(len(List)):
                this = List[i]
                if this['id'] == target:
                    name = this['name']
                    desp = this['desp']
                    level = this['level']
                    assigness = this['assigness']
                    deadline = this['deadline']
                    sublist = this['sublist']
                    self.logger.log('获取指定主任务 | 成功')
                    return [name, desp, level, assigness, deadline, sublist]
            self.logger.warn('获取指定主任务 | 未找到')
            return None
        except BaseException as ex:
            self.logger.error(f'获取指定主任务 | 失败：\n    {ex}')
    #
    def getSub(self, sub_parent):
        try:
            List = _Helper.getList(self.json_file_path)
            for this in List:
                if this['id'] == sub_parent:
                    self.logger.log('获取指定子任务 | 成功')
                    return this['sublist']
            self.logger.warn('获取指定子任务 | 未找到')
            return None
        except BaseException as ex:
            self.logger.error(f'获取指定子任务 | 失败：\n    {ex}')
    # End: Get #
    #
    # Start: Add #
    def addMain(self, name, desp, level, assigness, deadline):
        try:
            List = _Helper.getList(self.json_file_path)
            List.append({
                'name': name, 
                'desp': desp, 
                'level': level, 
                'assigness': assigness, 
                'deadline': deadline, 
                'sublist': [],
                'id': len(List) + 1
            })
            with open(self.json_file_path, 'w', encoding='utf-8') as ListFile:
                ListFile.write(dumps(List, ensure_ascii=False, indent=4))
            self.logger.log(f'添加主任务 | 成功')
        except BaseException as ex:
            self.logger.error(f'添加主任务 | 失败：\n    {ex}')
    #
    def addSub(self, name, desp, level, assigness, deadline, parent):
        try:
            List = _Helper.getList(self.json_file_path)
            for this in List:
                if this['id'] == parent:
                    this['sublist']:list.append({
                        'name': name, 
                        'desp': desp, 
                        'level': level, 
                        'assigness': assigness, 
                        'deadline': deadline,
                        'sub_id': len(this['sublist']) + 1
                    })
            with open(self.json_file_path, 'w', encoding='utf-8') as ListFile:
                ListFile.write(dumps(List, ensure_ascii=False, indent=4))
            self.logger.log(f'添加子任务 | 成功')
        except BaseException as ex:
            self.logger.error(f'添加子任务 | 失败：\n    {ex}')
    # End: Add #
    #
    # Start: Edit #
    def editMain(self, targetID, newName=None, newDesp=None, newLevel=None, newAssigness=None, newDeadline=None):
        try:
            List = _Helper.getList(self.json_file_path)
            for this in List:
                if this['name'] == targetID:
                    if newName != None: this['name'] = newName
                    if newDesp != None: this['desp'] = newDesp
                    if newLevel != None: this['level'] = newLevel
                    if newAssigness != None: this['assigness'] = newAssigness
                    if newDeadline != None: this['deadline'] = newDeadline
                    break
            with open(self.json_file_path, 'w', encoding='utf-8') as ListFile:
                ListFile.write(dumps(List, ensure_ascii=False, indent=4))
            self.logger.log(f'编辑主任务 | 成功')
        except BaseException as ex:
            self.logger.error(f'编辑主任务 | 失败：\n    {ex}')
    #
    def editSub(self, mainID, targetID, newName=None, newDesp=None, newLevel=None, newAssigness=None, newDeadline=None):
        try:
            List = _Helper.getList(self.json_file_path)
            for this in List:
                if this['id'] == mainID:
                    for sub in this['sub']:
                        if sub['sub_id'] == targetID:
                            if newName != None: sub['name'] = newName
                            if newDesp != None: sub['desp'] = newDesp
                            if newLevel != None: sub['level'] = newLevel
                            if newAssigness != None: sub['assigness'] = newAssigness
                            if newDeadline != None: sub['deadline'] = newDeadline
                            break
                    with open(self.json_file_path, 'w', encoding='utf-8') as ListFile:
                        ListFile.write(dumps(List, ensure_ascii=False, indent=4))
                    self.logger.log(f'编辑子任务 | 成功')
                    return
            self.logger.warn(f'编辑子任务 | 失败：未找到主任务')
        except BaseException as ex:
            self.logger.log(f'编辑子任务 | 失败：{ex}')
    # End: Edit #
    #
    # Start: Del #
    def delMain(self, targetID):
        try:
            List = _Helper.getList(self.json_file_path)
            newList = [item for item in List if item['id'] != targetID]
            with open(self.json_file_path, 'w', encoding='utf-8') as ListFile:
                ListFile.write(dumps(newList, ensure_ascii=False, indent=4))
            self.logger.log(f'删除主任务 | 成功')
        except BaseException as ex:
            self.logger.log(f'删除主任务 | 失败：{ex}')
    #
    def delSub(self, parentID, targetID):
        try:
            List = _Helper.getList(self.json_file_path)
            for main in List:
                if main['name'] == parentID:
                    newSub = [item for item in main['sublist'] if item['sub_id'] != targetID]
                    main['sublist'] = newSub
                    break
            with open(self.json_file_path, 'w', encoding='utf-8') as ListFile:
                ListFile.write(dumps(List, ensure_ascii=False, indent=4))
            self.logger.log(f'删除子任务 | 成功')
        except BaseException as ex:
            self.logger.log(f'删除子任务 | 失败：{ex}')

class _Helper():
    '''
    ! Only a class for help | Do Not Use in other Code !T
    '''
    def checkDir():
        if not exists('./data'): mkdir('data')
        if not exists('./data/quest'): mkdir('data/quest')
    def checkFile(path):
        if not exists(path):
            with open(path, 'w', encoding='utf-8') as ListFile:
                ListFile.write(dumps([]))
    #
    def getList(json_file_path) -> list:
        with open(json_file_path, 'r', encoding='utf-8') as ListFile:
            List = loads(ListFile.read())
            return List