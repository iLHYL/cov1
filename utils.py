import time
import pymysql

def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")

def get_conn():
    """

    :return:连接 ，游标
    """
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "803771",
        db = "cov2019",
        charset = "utf8"
    )

    cursor = conn.cursor()

    return conn,cursor

def close_conn(conn,cursor):
    cursor.close()
    conn.close()

def query(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),())的形式
    """
    conn,cursor = get_conn()
    cursor.execute(sql)
    res = cursor.fetchall()
    close_conn(conn,cursor)

    return res

def c1_query():
    """

    :return:返回div id = c1所需的数据
    """
    sql = "select sum(confirm_total),"\
    "(select suspect from history order by ds desc limit 1),"\
    "sum(heal_total),"\
    "sum(dead_total) "\
    "from details "\
    "where update_time = (select update_time from details order by update_time desc limit 1)"
    res = query(sql)
    return res[0]

def c2_query():
    """

    :return:返回省份现存确诊
    """
    sql = 'SELECT province,sum(confirm_total-heal_total-dead_total) from details '\
    'where update_time = (SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1) '\
    'GROUP BY province'
    res = query(sql)
    return res

def l1_query():
    """

    :return:l1所需的今日信息
    """
    sql = 'SELECT ds,confirm,suspect,heal,dead from history ORDER BY ds DESC LIMIT 7'
    res = query(sql)
    return res

def l2_query():
    """

    :return:l2所需的今日信息
    """
    sql = 'SELECT ds,confirm_add,suspect_add,heal_add,dead_add from history ORDER BY ds DESC LIMIT 7'
    res = query(sql)
    return res

def outcome_query():
    """

    :return:返回境外入境的人数
    """
    sql = "select province,confirm_total,confirm_add,heal_total from details where city ='境外输入'"\
    "AND update_time = (SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1)"
    res = query(sql)
    return res

def hotsearch_query():
    """

    :return: 返回r2所需的热搜数据
    """
    sql = 'select content from hotsearch order by id desc limit 20'
    res = query(sql)
    return res

if __name__ == '__main__':
    # print(l2_query())
    res = hotsearch_query()
    print(res)