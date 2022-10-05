from flask import jsonify, render_template
from config import *
from controllers import (
    usuario_controller,
    auth_controller,
    actividade_controller
)


@app.route('/', methods=['GET'])
@app.route('/inicio', methods=['GET'])
def inicio():
    return render_template('inicio.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)