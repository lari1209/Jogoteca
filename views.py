from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from dao import UsuarioDao
from jogoteca import db, app

usuario_dao = UsuarioDao(db)


# Tela inicial
@app.route('/')
def index():
    return render_template('home.html', titulo='Faça o login')


# Página após logar
@app.route('/page')
def page():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('page')))
    return render_template('page.html')


# Página de login
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


# Autenticação das credenciais do usuário
@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'], request.form['senha'])
    if usuario:
        # se o id e a senha estiverem corretos ir para a proxima página -> page
        if usuario.senha == request.form['senha'] and request.form['usuario'] == usuario.id:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Algo está errado, tente de novo!')
        return redirect(url_for('login'))

# Logout da conta
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))
