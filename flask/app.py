from flask import (
    Flask, make_response, render_template)

app = Flask(__name__)


@app.route('/')
def root():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('index', 'set_by_index')
    return resp


@app.route('/esi/')
def esi():
    resp = make_response("Content from esi", 200)
    resp.set_cookie('esi', 'set_by_esi_response')
    return resp


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
