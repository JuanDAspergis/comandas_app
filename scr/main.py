from flask import Flask, render_template, session
from settings import HOST, PORT, DEBUG, TEMPO_SESSION
from datetime import timedelta
import os

from mod_index.index import bp_index
from mod_funcionario.funcionario import bp_funcionario
from mod_cliente.cliente import bp_cliente
from mod_produto.produto import bp_produto
from mod_erro.erro import bp_erro
from mod_login.login import bp_login

app = Flask(__name__)

app.secret_key = os.urandom(12).hex()

@app.before_request
def before_request():
    session.permanet = True
    session['tempo'] = int(TEMPO_SESSION)
    app.permanet_session_lifetime = timedelta(minutes=session['tempo'])

app.register_blueprint(bp_login)
app.register_blueprint(bp_index)
app.register_blueprint(bp_funcionario)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_produto)
app.register_blueprint(bp_erro)


if __name__ == "__main__":
    app.run(host = HOST, port = PORT, debug = DEBUG)

app.config.update(
    SESSION_COOKIE_SAMESITE='None',
    SESSION_COOKIE_SECURE='True'
)