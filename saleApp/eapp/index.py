from flask import render_template, request
from werkzeug.utils import redirect
from flask_login import login_user, logout_user
from eapp import app,dao,login


@app.route('/')
def index():
    products = dao.load_products(cate_id=request.args.get('category_id'),
                                 kw=request.args.get('kw'),
                                 page=request.args.get('page'))

    return render_template('index.html', products=products)

@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/register')
def register_view():
    return render_template('register.html')

@app.context_processor
def common_responses():
    return {
        'categories': dao.load_categories()
    }

@login.user_loader
def load_user(id):
    return dao.get_user_by_id(id)

@app.route('/login', methods=['POST'])
def login_process():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)
    next = request.args.get('next')
    return redirect(next if next else '/admin')

@app.route('/logout')
def logout_process():
    logout_user()
    return redirect('/login')

if __name__ == '__main__':
    from eapp import admin
    app.run(debug=True)