from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策

'''
READ: インストール状況を取得
'''
@app.route('/status', methods=['GET'])
def post_json():
    req_json = request.get_json()
    return jsonify(req_json)


'''
UPDATE: インストールの状況を追加/更新
'''
@app.route('/status', methods=['POST'])
def update_status():
    req_json = request.get_json()
    return jsonify(req_json)


'''
READ: インストール設定を取得
'''
@app.route('/settings', methods=['GET'])
def read_setting():
    with open('config.yaml') as f:
        file_content = yaml.load(f, Loader=yaml.SafeLoader)
    return jsonify(file_content)
