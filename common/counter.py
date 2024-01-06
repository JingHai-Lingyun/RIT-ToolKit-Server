from json import loads, dumps
from os.path import exists, abspath
from os import mkdir

from .logger import lyLogger


class Counter():
    # 获得 Logger 操作器
    logger = lyLogger('log/', 'server.log', 'Counter')
    json_file_path = './data/counter/list.json'
    #
    def __init__(self):
        if not exists('./data'): mkdir('data')
        if not exists('./data/counter'): mkdir('./data/counter')
        if not exists(self.json_file_path):
            with open(self.json_file_path, 'w', encoding='utf-8') as ListFile:
                ListFile.write(dumps(
                    [
                        {
                            'name': '\u8fdc\u53e4\u6b8b\u9ab8\u6316\u6398\u91cf',
                            'value': 0,
                            'ID': 'LingyunAwA',
                            'cid': 1,
                        }
                    ]
                ))
        else:
            with open(self.json_file_path, 'r', encoding='utf-8') as ListFile:
                fc = ListFile.read()
            if fc == None or fc == '':
                with open(self.json_file_path, 'w', encoding='utf-8') as ListFile:
                    ListFile.write(dumps(
                        [
                            {
                                'name': '\u8fdc\u53e4\u6b8b\u9ab8\u6316\u6398\u91cf',
                                'value': 0,
                                'ID': 'LingyunAwA',
                                'cid': 1,
                            }
                        ]
                    ))
        self.logger.log('初始化计数器')
    #
    def getall(self):
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as ListFile:
                data = loads(ListFile.read())
                self.logger.log('获取全部数据 | 成功')
                return data
        except:
            self.logger.warn('获取全部数据 | 未找到文件')
            return {}
    #
    def get(self, name):
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as ListFile:
                List = loads(ListFile.read())
        except:
            self.logger.warn(f'获取指定数据 | 错误：未找到文件 {abspath(self.json_file_path)}')
            # raise FileNotFoundError(f'Missing Data File: {abspath(self.json_file_path)} is not exists.')
            return None
        for counter in List:
            if counter['cid'] == int(name):
                self.logger.log('获取指定数据 | 成功')
                return [counter['value'], counter['id']]
        self.logger.warn('获取全部数据 | 未找到数据')
        return None
    #
    def set(self, name, value, id):
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as ListFile:
                List = loads(ListFile.read())
            for counter in List:
                if counter['cid'] == int(name):
                    counter['value'] = value
                    counter['ID'] = id
                    break
            with open(self.json_file_path, 'w', encoding='utf-8') as ListFile:
                ListFile.write(dumps(List))
            self.logger.log('设置指定数据 | 成功')
        except BaseException as ex:
            self.logger.error(f'设置指定数据 | 失败，错误为：\n    {ex}')
    #
    def join(self, name, value, id):
        cid = _Helper().genCID()
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as ListFile:
                List:list = loads(ListFile.read())
            List.append({
                'name': name,
                'value': value,
                'ID': id,
                'cid': cid,
            })
            with open(self.json_file_path, 'w', encoding='utf-8') as ListFile:
                ListFile.write(dumps(List))
            _Helper().addCID()
            self.logger.log('加入指定数据 | 成功')
        except BaseException as ex:
            self.logger.error(f'加入指定数据 | 失败，错误为：\n    {ex}')
    #
    def remove(self, name):
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as ListFile:
                List = loads(ListFile.read())
            self.logger.debug(List)
            updated_list = [counter for counter in List if counter['cid'] != int(name)]
            with open(self.json_file_path, 'w', encoding='utf-8') as ListFile:
                ListFile.write(dumps(updated_list))
            _Helper().minusCID()
            self.logger.log('删除指定数据 | 成功')
        except BaseException as ex:
            self.logger.error(f'删除指定数据 | 失败，错误为：\n    {ex}')

class _Helper():
    num_file_path = './data/counter/num.txt'
    def addCID(self):
        with open(self.num_file_path, 'r', encoding='utf-8') as NumFile:
            num = int(NumFile.read())
        num += 1
        with open(self.num_file_path, 'w', encoding='utf-8') as NumFile:
            NumFile.write(str(num))
    #
    def genCID(self):
        with open(self.num_file_path, 'r', encoding='utf-8') as NumFile:
            num = int(NumFile.read())
        num += 1
        return num
    #
    def minusCID(self):
        with open(self.num_file_path, 'r', encoding='utf-8') as NumFile:
            num = int(NumFile.read())
        num -= 1
        with open(self.num_file_path, 'w', encoding='utf-8') as NumFile:
            NumFile.write(str(num))