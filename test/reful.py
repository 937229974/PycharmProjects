import flask
from flask import request, app, jsonify

server = flask.Flask(__name__)

@server.route('/addTaskQueue', methods=['POST'])
def create_task():
    if request.method == 'POST':
        # p =request.get_data()
        p = request.form['mobile']
        # if not request.json or not 'title' in request.json:
        print(p)
    return jsonify({'task': "1"})
if __name__ == '__main__':
    server.run(debug=True, port=8000, host='0.0.0.0')