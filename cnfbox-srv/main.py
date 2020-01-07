from flask import Flask, request, jsonify
import pymysql.cursors
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策

connection = pymysql.connect(host=os.getenv('DB_HOST'),
                             user=os.getenv('DB_USER'),
                             password=os.getenv('DB_PASSWD'),
                             db=os.getenv('DB_NAME'),
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


@app.route('/', methods=['GET'])
def index():
    return 'It works'


@app.route('/conf/<int:conf_id>', methods=['GET'])
def read_conf(conf_id):
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id` FROM `config` WHERE `id`=%d AND `type`='kickstart'"
        cursor.execute(sql, int(conf_id))
        result = cursor.fetchone()
    return jsonify(result)


@app.route('/conf', methods=['POST'])
def create_conf():
    req_json = request.get_json()
    # 書き込み
    # 201 Created
    return jsonify(req_json)


@app.route('/conf/<int:id>', methods=['PUT'])
def update_status():
    req_json = request.get_json()
    # 書き込み
    # 200 Update
    return jsonify(req_json)


if __name__ == '__main__':
    app.run(debug=True)
