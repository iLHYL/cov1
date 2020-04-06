import time
import pymysql
import traceback

#建立数据库连接
from get_info_py.getTencentInfo import get_baidu_hot,get_tencent_data


def get_conn():
    conn = pymysql.connect('localhost', 'root', '803771', 'cov2019', charset='utf8')
    cursor = conn.cursor()

    return conn, cursor

# 关闭数据库连接
def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

#更新每日详情
def update_details():
    """
    更新details表
    """

    cursor = None
    conn = None
    try:
        li = get_tencent_data()[1]
        conn, cursor = get_conn()
        sql = "insert into details(update_time,province,city,confirm_add,confirmcuts_add,confirm_total,suspect_total,dead_total,heal_total)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = 'select %s = (select update_time from details order by id desc limit 1)'  # 对比当前最大时间戳
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新最新数据")
            for item in li:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}更新最新数据完毕")
        else:
            print(f"{time.asctime()}已是最新数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

# 更新历史数据
def update_history():
    """
    更新历史数据
    """
    cursor = None
    conn = None

    try:
        dic = get_tencent_data()[0]
        conn,cursor = get_conn()
        print(f"{time.asctime()}开始更新历史数据")
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirm from history where ds = %s"
        for k, v in dic.items():
            if not cursor.execute(sql_query, k):
                cursor.execute(sql, [k, v.get('confirm'), v.get('suspect'), v.get('heal'), v.get('dead'),
                                     v.get('confirm_add'), v.get('suspect_add'), v.get('heal_add'), v.get('dead_add')])
        conn.commit()
        print(f"{time.asctime()}更新历史数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

# 插入历史数据
def insert_history():
    """
    插入历史数据
    """
    cursor = None
    conn = None
    conn, cursor = get_conn()

    try:
        dic = get_tencent_data()[0]
        print(f"{time.asctime()}开始插入历史数据")
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for k, v in dic.items():
            cursor.execute(sql,
                           [k, v.get('confirm'), v.get('suspect'), v.get('heal'), v.get('dead'), v.get('confirm_add'),
                            v.get('suspect_add'), v.get('heal_add'), v.get('dead_add')])
        conn.commit()
        print(f"{time.asctime()}插入历史数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)



def update_baidu_hot():
    content = get_baidu_hot()
    conn = None
    cursor = None
    sql = 'insert into hotsearch(dt,content) values(%s,%s)'
    try:
        conn,cursor = get_conn()
        print(f"{time.asctime()}开始更新热搜数据")
        ct = time.strftime("%Y-%m-%d %X")
        for i in content:
            cursor.execute(sql,(ct,i))
        conn.commit()
        print(f"{time.asctime()}数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)

if __name__ == '__main__':
    update_details()
    update_history()
    update_baidu_hot()