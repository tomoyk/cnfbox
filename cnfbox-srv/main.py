from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策


@app.route('/', methods=['GET'])
def index():
    return 'It works'


@app.route('/conf/<int:id>', methods=['GET'])
def post_json(id):
    return f'todo: get conf {id}'


@app.route('/conf', methods=['GET'])
def create_conf():
    return 'There is nothing'


@app.route('/conf', methods=['POST'])
def update_status():
    req_json = request.get_json()
    return jsonify(req_json)


if __name__ == '__main__':
    app.run(debug=True)
