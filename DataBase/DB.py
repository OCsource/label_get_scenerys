import pymysql
from label_get_scenerys.uitls import logUtil

logger = logUtil.getLogger(0)

class operateDB:
    def __init__(self):
        self.__dbName = 'qunar'
        self.__user = 'root'
        self.__password = '123456'
        self.__host = 'localhost'
        self.__char = 'utf8'

    # 查询某标签的景点信息
    # 参数：标签名
    # 返回成功标签相应的景点名称，失败false
    def sreachSceneryByLabel(self, label):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "select scenery_name from scenery_table where scenery_number in (select scenery_number from scenery_words where word = '%s')"%(label)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            logger.error(label+ ":景点查找失败")
            return False
        finally:
            db.close()

    # 查找攻略所有景点
    # 参数：攻略编号
    # 返回：成功相应的景点名称，失败false
    def getAllLink(self,strategy_number=0):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        if strategy_number == 0:
            sql = "SELECT * FROM strategy_scenery WHERE 1;"
        else:
            sql = "SELECT * FROM strategy_scenery WHERE stratery_number = '%s';" % (strategy_number)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            logger.error(strategy_number + ":景点攻略查找失败")
            return False
        finally:
            db.close()

    # 获取景点名称
    # 返回：成功所有景点名，失败false
    def sreachSceneryName(self):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT scenery_name FROM scenery_table WHERE 1;"
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            logger.error("景点查找失败")
            return False
        finally:
            db.close()
