from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策

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


@app.route('/settings', methods=['GET'])
def read_setting():
    """ READ: インストール設定を取得 """
    with open('config.yaml') as f:
        file_content = yaml.load(f, Loader=yaml.SafeLoader)
    return jsonify(file_content)
