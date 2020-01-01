from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策


@app.route('/', methods=['GET'])
def index():
    return 'It works'


@app.route('/status', methods=['GET'])
def post_json():
    """ READ: インストール状況を取得 """
    req_json = request.get_json()
    return jsonify(req_json)


@app.route('/status', methods=['POST'])
def update_status():
    """ UPDATE: インストールの状況を追加/更新 """
    req_json = request.get_json()
    return jsonify(req_json)


if __name__ == '__main__':
    app.run(debug=True)
