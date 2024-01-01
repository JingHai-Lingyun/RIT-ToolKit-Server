from os.path import exists
from os import mkdir
from datetime import datetime

class lyLogger():
    '''
    LingyunAwA's Logger
    '''
    def __init__(self, file_dir = 'log/', file_name = 'server.log', module = 'Self'):
        self.dir = file_dir
        self.name = file_name
        self.module = module
        # 检查路径
        if not exists(self.dir):
            mkdir(self.dir)
        # 检查文件
        try:
            with open(f'{self.dir}/{self.name}', 'a', encoding='utf-8') as log:
                log.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] [INFO] [Self] 日志记录器被加载!\n')
        except FileNotFoundError:
            with open(f'{self.dir}/{self.name}', 'w', encoding='utf-8') as log:
                log.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] [INFO] [Self] 日志记录器被加载!\n')
    #
    def log(self, msg):
        with open(f'{self.dir}/{self.name}', 'a', encoding='utf-8') as log:
            log.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] [INFO] [{self.module}] {msg}\n')
    #
    def warn(self, msg):
        with open(f'{self.dir}/{self.name}', 'a', encoding='utf-8') as log:
            log.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] [WARN] [{self.module}] {msg}\n')
    #
    def error(self, msg):
        with open(f'{self.dir}/{self.name}', 'a', encoding='utf-8') as log:
            log.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] [ERROR] [{self.module}] {msg}\n')
    #
    def debug(self, msg):
        with open(f'{self.dir}/{self.name}', 'a', encoding='utf-8') as log:
            log.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] [DEBUG] [{self.module}] {msg}\n')
    def clearAll(self):
        with open(f'{self.dir}/{self.name}', 'w', encoding='utf-8') as log:
            log.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] [INFO] [Self] 日志已被清空！\n')