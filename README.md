---
**将景点标签相似度较高的找出来**
---

入口函数：main.py

包说明：

mappingScenery：通过标签名找到景点

relatedSites：寻找关联景点

DataBase：访问数据库

logs：存放错误日记

utils：存放工具的地方

---
**技术栈**
---

python(python3.7 x64)：有python的一定基础，https://www.runoob.com/python/python-tutorial.html

---
**包的层次结构**
---

clustering_scenery_tags ---- relatedSites ---- Apriori.py

                                        ---- dealData.py
                                        
                                        ---- matchingFunc.py

                        ---- DataBase ---- DB.py
                  
                        ---- logs ---- data_log.log
                  
                                  ---- DB_log.log
                  
                        ---- utils ---- logUtil.py
                  
                        ---- main.py
                  
                        ----README.md
       
---
**依赖包**
---

pymysql：用于python连接数据库
