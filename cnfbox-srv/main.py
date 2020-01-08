from flask import Flask, request, jsonify
import pymysql.cursors
import os
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策

connection = pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWD'),
    db=os.getenv('DB_NAME'),
    unix_socket=os.getenv('UNIX_SOCKET') if os.getenv('UNIX_SOCKET') else None,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)


@app.route('/', methods=['GET'])
def index():
    return 'It works'


# DOWNLOAD NORMAL
@app.route('/conf/<int:conf_id>', methods=['GET'])
def read_conf(conf_id):
    with connection.cursor() as cursor:
        sql = "SELECT `content` FROM `config` WHERE `id`=%s"
        cursor.execute(sql, str(conf_id))
        result = cursor.fetchone()
    str_json = result.get('content')
    return jsonify(json.loads(str_json))


def get_content(req_id: int):
    with connection.cursor() as cursor:
        sql = "SELECT `content` FROM `config` WHERE `id`=%s"
        cursor.execute(sql, str(req_id))
    return cursor.fetchone()


# DOWNLOAD KICKSTART
@app.route('/conf/<int:conf_id>/kickstart', methods=['GET'])
def read_conf_ks(conf_id):
    raw_json = get_content(conf_id).get('content')
    params = json.loads(raw_json)

    import crypt
    passwords = params['user']['password']
    for k_user, v_pwd in passwords:
        params['user']['password'][k_user] = crypt.crypt(
            v_pwd, crypt.METHOD_SHA512)

    return render_template('kickstart.txt', val=params)


# DOWNLOAD PRESEED
@app.route('/conf/<int:conf_id>/preseed', methods=['GET'])
def read_conf_pr(conf_id):
    with connection.cursor() as cursor:
        sql = "SELECT `content` FROM `config` WHERE `id`=%s"
        cursor.execute(sql, str(conf_id))
        result = cursor.fetchone()
    str_json = result.get('content')
    return jsonify(json.loads(str_json))


# UPLOAD
@app.route('/conf', methods=['POST'])
def create_conf():
    req_data = request.get_data()
    req_txt = req_data.decode('utf-8')
    # assert json.loads(req_json), 'Fatal Error'
    with connection.cursor() as cursor:
        sql = "INSERT INTO config (`content`) VALUES (%s)"
        cursor.execute(sql, req_txt)

    connection.commit()
    return jsonify({"status": "ok"})


@app.route('/conf/<int:id>', methods=['PUT'])
def update_status():
    req_json = request.get_json()
    # 書き込み
    # 200 Update
    return jsonify({"status": "ok"})


@app.errorhandler(404)
def error_404():
    response = jsonify({"status": "not found"})
    return response, 404


if __name__ == '__main__':
    app.run(debug=True)
