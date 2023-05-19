from crud_com_flask.app import app, db
from crud_com_flask.models.table import Soma
from flask import render_template, request, redirect


# Create nos leva ao index onde inserimos os numeros a serem somados
@app.route('/')
@app.route('/index/')
@app.route('/create/')
def create():
    return render_template("index.html")


# Calcular faz a insercao dos numeros na tabela
@app.route('/calcular/', methods=['POST'])
def calcular():
    n1 = int(request.form["numero1"])
    n2 = int(request.form["numero2"])
    soma = Soma(n1=n1, n2=n2)
    db.session.add(soma)
    db.session.commit()
    return redirect('/read/')


# read faz a exibicao da tabela
@app.route('/read/', methods=['GET'])
def read():
    somas = Soma.query.all()
    return render_template("read.html", tabela=somas)


# receive abre o arquivo de atualizacao dos numeros
@app.route("/receive/", methods=["POST"])
def receive():
    item_id = request.form['upgrade']
    item = Soma.query.get(item_id)
    return render_template('update.html', item=item, item_id=item_id)


# upgrade atualiza os valores
@app.route("/upgrade/<key>", methods=["POST"])
def upgrade(key):
    novovalor1 = int(request.form['numero1'])
    novovalor2 = int(request.form['numero2'])
    item = Soma.query.get(key)
    item.numero1 = novovalor1
    item.numero2 = novovalor2
    item.soma = novovalor1 + novovalor2
    db.session.commit()
    return redirect('/read/')


# delete exclui o item da linha
@app.route("/delete/", methods=["POST"])
def delete():
    item_id = request.form['del']
    item = Soma.query.get(item_id)

    db.session.delete(item)
    db.session.commit()

    return render_template("delete.html")


# deleteAll serve para reiniciar o banco por completo
@app.route("/deleteall/", methods=["POST"])
def deleteall():
    with app.app_context():
        db.drop_all()
        db.create_all()

    return render_template("index.html")

