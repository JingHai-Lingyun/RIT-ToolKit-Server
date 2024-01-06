from flask import Flask, request, make_response as mr, abort
from flask_cors import CORS

from common.logger import lyLogger
from common.counter import Counter
from common.waypointer import Waypointer
from common.quester import Quester

app = Flask(__name__)
CORS(app, methods=['GET', 'POST', 'PATCH', 'DELETE'])

# 配置 Logger 操作器
logger = lyLogger('log/', 'server.log', 'Server')

# 配置 Counter 操作器
counter = Counter()
# 配置 Wayoint 操作器
waypointer = Waypointer()
# 配置 Quester 操作器
quester = Quester()

@app.route('/')
def index():
    return '你可以访问到接口'

# - Counter - #
@app.route('/counter/getCounter')
def get_counter():
    # 获取参数
    counterName = request.args.get('counterCid')
    updateUserID = request.args.get('updateUserID')
    # 鉴权
    if counterName is None:
        abort(400, '缺少参数 counterName')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        logger.log(f'{updateUserID} 获取计数器：{counterName}')
        counterValue = counter.get(counterName)
        return str(counterValue)
    except BaseException as ex:
        logger.error(f'{updateUserID} 获取计数器 {counterName} 失败：\n    {ex}')
        abort(500, 'FAIL')
#
@app.route('/counter/getAllCounter')
def get_all_counter():
    # 获取参数
    updateUserID = request.args.get('updateUserID')
    # 鉴权
    if updateUserID == None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        logger.log(f'{updateUserID} 获取全部计数器')
        counterValue = counter.getall()
        return str(counterValue)
    except BaseException as ex:
        logger.error(f'{updateUserID} 获取全部计数器失败：\n    {ex}')
        abort(500, 'FAIL')
#
@app.route('/counter/addCounter', methods = ['POST'])
def add_counter():
    # 获取参数
    counterName = request.form.get('counterName')
    updateUserID = request.form.get('updateUserID')
    # 鉴权
    if counterName is None:
        abort(400, '缺少参数 counterName')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        logger.log(f'{updateUserID} 添加计数器：{counterName}')
        counter.join(counterName, 0, updateUserID)
        return 'OK'
    except BaseException as ex:
        logger.error(f'{updateUserID} 添加计数器 {counterName} 失败：\n    {ex}')
        abort(500, 'FAIL')
#
@app.route('/counter/setCounter', methods = ['PATCH'])
def set_counter():
    # 获取参数
    counterName = request.form.get('counterCid')
    counterValue = request.form.get('counterValue')
    updateUserID = request.form.get('updateUserID')
    # 鉴权
    if counterName is None or counterValue is None:
        abort(400, '缺少参数 counterName 或 counterValue')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        logger.log(f'{updateUserID} 设置计数器：{counterName} 为 {counterValue}')
        counter.set(counterName, counterValue, updateUserID)
        return 'OK'
    except BaseException as ex:
        logger.error(f'{updateUserID} 设置计数器 {counterName} 为 {counterValue} 失败：\n    {ex}')
        abort(500, 'FAIL')
#
@app.route('/counter/rmCounter', methods = ['DELETE'])
def rm_counter():
    # 获取参数
    counterName = request.form.get('counterCid')
    updateUserID = request.form.get('updateUserID')
    # 鉴权
    if counterName is None:
        abort(400, '缺少参数 counterName')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        logger.log(f'{updateUserID} 删除计数器：{counterName}')
        counter.remove(counterName)
        return 'OK'
    except BaseException as ex:
        logger.error(f'{updateUserID} 删除计数器 {counterName} 失败：\n    {ex}')
        abort(500, 'FAIL')
# ----------- #

# - Waypoint - #
@app.route('/waypoint/getAllWaypoint')
def getAllWaypoint():
    # 获取参数
    updateUserID = request.args.get('updateUserID')
    # 鉴权
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    logger.log(f'{updateUserID} 获取所有航点')
    resp = waypointer.getall()
    return str(resp)

@app.route('/waypoint/addWaypoint', methods = ['POST'])
def addWaypoint():
    # 获取参数
    waypointName = request.form.get('waypointName')
    waypointX = request.form.get('X')
    waypointY = request.form.get('Y')
    waypointZ = request.form.get('Z')
    waypointDim = request.form.get('Dim')
    updateUserID = request.form.get('updateUserID')
    # 鉴权
    if waypointName is None or waypointX is None or waypointY is None or waypointZ is None or waypointDim is None:
        abort(400, '缺少参数 waypointName 或 X 或 Y 或 Z 或 Dim')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        waypointer.join(waypointName, waypointX, waypointY, waypointZ, waypointDim, updateUserID)
        logger.log(f'{updateUserID} 添加航点 {waypointName}')
        return 'OK'
    except BaseException as ex:
        logger.error(f'{updateUserID} 添加航点 {waypointName} 失败：\n    {ex}')
        abort(500, 'FAIL')

@app.route('/waypoint/rmWaypoint', methods = ['DELETE'])
def rmWaypoint():
    # 获取参数
    waypointName = request.form.get('waypointCid')
    logger.debug(waypointName)
    updateUserID = request.form.get('updateUserID')
    # 鉴权
    if waypointName is None:
        abort(400, '缺少参数 waypointCid')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        waypointer.remove(waypointName)
        logger.log(f'{updateUserID} 删除航点 {waypointName}')
        return 'OK'
    except BaseException as ex:
        logger.error(f'{updateUserID} 删除航点 {waypointName} 失败：\n    {ex}')
        abort(500, 'FAIL')
# ------------ #

# - Quest - #
@app.route('/quest/getQuestList')
def getQuestList():
    # 获取参数
    updateUserID = request.args.get('updateUserID')
    # 鉴权
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        questList = quester.getSimple()
        logger.log(f'{updateUserID} 获取全部任务')
        return questList
    except BaseException as ex:
        logger.error(f'{updateUserID} 获取全部任务 失败：\n    {ex}')
        abort(500, 'FAIL')

@app.route('/quest/getMain')
def getMainQuest():
    # 获取参数
    questID = request.args.get('questID')
    updateUserID = request.args.get('updateUserID')
    # 鉴权
    if questID is None:
        abort(400, '缺少参数 questID')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        questList = quester.getMain(questID)
        return questList
    except BaseException as ex:
        logger.error(f'{updateUserID} 获取指定主任务 失败：\n    {ex}')
        abort(500, 'FAIL')

@app.route('/quest/getSub')
def getSubQuest():
    # 获取参数
    parent = request.args.get('parent')
    updateUserID = request.args.get('updateUserID')
    # 鉴权
    if parent is None:
        abort(400, '缺少参数 parent')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        subQuestList = quester.getSub(parent)
        logger.log(f'{updateUserID} 获取指定子任务')
        return subQuestList
    except BaseException as ex:
        logger.error(f'{updateUserID} 获取指定子任务 失败：\n    {ex}')
        abort(500, 'FAIL')

@app.route('/quest/addMain', methods=['POST'])
def addMainQuest():
    # 获取参数
    questName = request.form.get('questName')
    questDesc = request.form.get('questDesc')
    questLevel = request.form.get('questLevel')
    questAssigness = request.form.get('questAssigness')
    questDeadline = request.form.get('questDeadline')
    updateUserID = request.form.get('updateUserID')
    # 鉴权
    if questName is None or questDesc is None or questLevel is None or questDeadline is None or questAssigness is None:
        abort(400, '缺少参数 questName 或 questDesc 或 questLevel 或 questDeadline 或 questAssigness')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        quester.addMain(questName, questDesc, questLevel, questAssigness, questDeadline)
        logger.log(f'{updateUserID} 添加主任务')
        return 'OK'
    except BaseException as ex:
        logger.error(f'{updateUserID} 添加主任务 失败：\n    {ex}')
        abort(500, 'FAIL')

@app.route('/quest/addSub', methods=['POST'])
def addSubQuest():
    # 获取参数
    questName = request.form.get('questName')
    questDesc = request.form.get('questDesc')
    questLevel = request.form.get('questLevel')
    questDeadline = request.form.get('questDeadline')
    questAssigness = request.form.get('questAssigness')
    questParent = request.form.get('questParent')
    updateUserID = request.form.get('updateUserID')
    # 鉴权
    if questName is None or questDesc is None or questLevel is None or questDeadline is None or questAssigness is None or questParent is None:
        abort(400, '缺少参数 questName 或 questDesc 或 questLevel 或 questDeadline 或 questAssigness 或 questParent')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        quester.addSub(questName, questDesc, questLevel, questAssigness, questDeadline, questParent)
        logger.log(f'{updateUserID} 添加子任务')
        return 'OK'
    except BaseException as ex:
        logger.error(f'{updateUserID} 添加子任务 失败：\n    {ex}')
        abort(500, 'FAIL')

@app.route('/quest/editMain', methods=['PATCH'])
def editMainQuest():
    # 获取参数
    questID = request.form.get('questID')
    questName = request.form.get('questName')
    questDesc = request.form.get('questDesc')
    questLevel = request.form.get('questLevel')
    questDeadline = request.form.get('questDeadline')
    questAssigness = request.form.get('questAssigness')
    updateUserID = request.form.get('updateUserID')
    # 鉴权
    if questID is None:
        abort(400, '缺少参数 questID')
    if questName is None and questDesc is None and questLevel is None and questDeadline is None and questAssigness is None:
        abort(400, '未提供 questName 或 questDesc 或 questLevel 或 questDeadline 或 questAssigness 中的任何一项')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        quester.editMain(questID, questName, questDesc, questLevel, questAssigness, questDeadline)
        logger.log(f'{updateUserID} 编辑主任务')
        return 'OK'
    except BaseException as ex:
        logger.error(f'{updateUserID} 编辑主任务 失败：\n    {ex}')
        abort(500, 'FAIL')

@app.route('/quest/editSub', methods=['PATCH'])
def editSubQuest():
    # 获取参数
    questID = request.form.get('questID')
    subquestID = request.form.get('subquestID')
    subquestName = request.form.get('subquestName')
    subquestDesc = request.form.get('subquestDesc')
    subquestLevel = request.form.get('subquestLevel')
    subquestDeadline = request.form.get('subquestDeadline')
    subquestAssigness = request.form.get('subquestAssigness')
    updateUserID = request.form.get('updateUserID')
    # 鉴权
    if questID is None or subquestID is None:
        abort(400, '缺少参数 questID 或 subquestID')
    if subquestName is None and subquestDesc is None and subquestLevel is None and subquestDeadline is None and subquestAssigness is None:
        abort(400, '未提供 subquestName 或 subquestDesc 或 subquestLevel 或 subquestDeadline 或 subquestAssigness 中的任何一项')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        quester.editSub(questID, subquestID, subquestName, subquestDesc, subquestLevel, subquestAssigness, subquestDeadline)
        logger.log(f'{updateUserID} 编辑子任务')
        return 'OK'
    except BaseException as ex:
        logger.error(f'{updateUserID} 编辑子任务 失败:\n    {ex}')
        abort(500, 'FAIL')

@app.route('/quest/rmMain', methods=['DELETE'])
def rmMainQuest():
    # 获取参数
    questID = request.form.get('questID')
    updateUserID = request.form.get('updateUserID')
    # 鉴权
    if questID is None:
        abort(400, '缺少参数 questID')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        quester.delMain(questID)
        logger.log(f'{updateUserID} 删除主任务(id: {questID})')
        return 'OK'
    except BaseException as ex:
        logger.error(f'{updateUserID} 删除主任务(id: {questID}) 失败:\n    {ex}')
        abort(500, 'FAIL')

@app.route('/quest/rmSub', methods=['DELETE'])
def rmSubQuest():
    # 获取参数
    questID = request.form.get('questID')
    subquestID = request.form.get('subquestID')
    updateUserID = request.form.get('updateUserID')
    # 鉴权
    if questID is None or subquestID is None:
        abort(400, '缺少参数 questID 或 subquestID')
    if updateUserID is None or updateUserID == 'null':
        abort(403, '缺少参数 updateUserID')
    # 操作
    try:
        quester.delSub(questID, subquestID)
        logger.log(f'{updateUserID} 删除子任务(id: {subquestID}, from id: {questID})')
        return 'OK'
    except BaseException as ex:
        logger.error(f'{updateUserID} 删除子任务(id: {subquestID}, from id: {questID}) 失败:\n    {ex}')
        abort(500, 'FAIL')
# --------- #

@app.route('/log/clearLog')
def clearLog():
    # 获取参数
    auth = request.args.get('auth')
    if auth != '2M$K/m-`iymWXb}[7oRG1.iS-~n.9yIqy-^EK4A7<4R_s]e}T|Jy4E3tb/KVz1J-':
        return mr('Forbidden', 403)
    logger.clearAll()
    return 'OK'

if __name__ == '__main__':
    logger.log('服务器启动')
    # app.run(host='172.16.6.163',port=3930)
    app.run(port=3930)