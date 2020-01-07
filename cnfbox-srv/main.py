from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策


@app.route('/', methods=['GET'])
def index():
    return 'It works'


@app.route('/conf/<int:conf_id>', methods=['GET'])
def read_conf(conf_id):
    # 読み取り
    # 200 Fetch
    return f'todo: get conf {conf_id}'


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
