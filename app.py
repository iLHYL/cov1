import string
import time
from random import randint
from jieba.analyse import extract_tags
import utils
from flask import Flask
from flask import request,render_template
from flask import jsonify
app = Flask(__name__)
app.app_context().push()
@app.route('/')
def covindex():
    return render_template("main.html")

@app.route('/time')
def get_time():
    return utils.get_time()

@app.route('/c1')
def get_c1_data():
    data =  utils.c1_query()
    return jsonify({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3],})

@app.route('/c2')
def get_c2_data():
    res = []
    for tup in utils.c2_query():
        res.append({"name":tup[0],"value":tup[1]})
    print(type(jsonify({"data":res})))
    return jsonify({"data":res})

@app.route('/l1')
def get_l1_data():
    data = utils.l1_query()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    day.append(data[0][0].strftime("%m-%d"))
    if data[0][1]<data[1][1]:
        confirm.append(data[0][1]+data[1][1])
        suspect.append(data[0][2]+data[1][2])
        heal.append(data[0][3]+data[1][3])
        dead.append(data[0][4]+data[1][4])
    else:
        confirm.append(data[0][1])
        suspect.append(data[0][2])
        heal.append(data[0][3])
        dead.append(data[0][4])
    for a,b,c,d,e in data[1:]:
        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    day.reverse()
    confirm.reverse()
    suspect.reverse()
    heal.reverse()
    dead.reverse()
    return jsonify({'day':day,"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead})

@app.route('/l2')
def get_l2_data():
    data = utils.l2_query()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for a,b,c,d,e in data:

        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    day.reverse()
    confirm.reverse()
    suspect.reverse()
    heal.reverse()
    dead.reverse()
    return jsonify({'day':day,"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead})

@app.route('/r1')
def get_r1_data():
    res = utils.outcome_query()
    index = 1
    data = []
    for i in res:
        data.append(i)
        index +=1
    index = index - 1
    return jsonify({'data':data,'len':index})

@app.route('/r2')
def get_r2_data():
    data = utils.hotsearch_query()
    d = []
    print('hhhhh')
    for i in data:
        k = i[0].rstrip(string.digits) #移除数据中心的数字
        v = i[0][len(k):] #获取后尾的数字
        ks = extract_tags(k) #使用jieba获取关键字
        for j in ks:
            if not j.isdigit():
                d.append({'name':j,'value':v})
    d.reverse()
    # print(d[0:30])
    return jsonify({"kws":d[0:30]})


if __name__  == '__main__':
    app.run()
    # get_r2_data()
    # # a = get_l2_data()

