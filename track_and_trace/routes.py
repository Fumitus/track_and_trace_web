<<<<<<< HEAD
from flask import render_template, url_for, flash, redirect, request
from track_and_trace import app, db
from track_and_trace.forms import RegistrationForm, LoginForm, CodesForm, ProductForm
from track_and_trace.models import User, Product, Codes, Box_codes, Pallet_codes
from flask_login import login_user, current_user, logout_user, login_required
from track_and_trace.new_code import GenerateNewCode, CheckEnteredCode

@app.route("/")
@app.route("/home")
def home():
    form = ProductForm()
    codes = Codes.query.all()
    products = Product.query.all()

    return render_template('home.html', codes=codes, products=products, new_code=new_code)

@app.route("/about")
def about():
    products = Product.query.all()
    
    return render_template('about.html', title='About', products=products)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created. You can now log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unseccessful. Please check email and password', 'danger')
    return render_template('login.html', title='login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route("/codes/new", methods=['GET', 'POST'])
@login_required
def new_code():
    form = CodesForm()
    
    new_code = CheckEnteredCode()
    if form.validate_on_submit():
        product_id=Product.query.first()
        code = Codes(product_id=product_id.id, code=form.input_code.data, 
                        new_code=new_code, user_id=current_user.username)
        db.session.add(code)
        db.session.commit()
        flash('Code information was entered to Data Base!', 'success')
        return redirect(url_for('home'))
    return render_template('work_with_codes.html', title='Codes', form=form)

@app.route("/product/new", methods=['GET', 'POST'])
@login_required
def new_product():
    products = Product.query.all()
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(product_name=form.product_name.data, 
                            product_batch=form.product_batch.data, 
                            expire_date=form.expire_date.data, user_id=current_user.id)
        db.session.add(product)
        db.session.commit()
        flash('Product information was entered to Data Base!', 'success')
        return redirect(url_for('new_code'))
    
    return render_template('work_with_products.html', title='Product data', products=products, form=form)

@app.route("/")
def current_product():
    products = Product.query.all()   
=======
from flask import render_template, url_for, flash, redirect, request
from track_and_trace import app, db
from track_and_trace.forms import RegistrationForm, LoginForm, CodesForm, ProductForm
from track_and_trace.models import User, Product, Codes, Box_codes, Pallet_codes
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    codes = Codes.query.all()
    products = Product.query.all()
    return render_template('home.html', codes=codes, products=products)

@app.route("/about")
def about():
    products = Product.query.all()
    
    return render_template('about.html', title='About', products=products)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created. You can now log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unseccessful. Please check email and password', 'danger')
    return render_template('login.html', title='login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route("/codes/new", methods=['GET', 'POST'])
@login_required
def new_code():
    form = CodesForm()
    if form.validate_on_submit():
        product_id=Product.query.first()
        code = Codes(product_id=product_id.id, code=form.input_code.data, 
                        new_code='need_to_be_generated', user_id=current_user.username)
        db.session.add(code)
        db.session.commit()
        flash('Code information was entered to Data Base!', 'success')
        return redirect(url_for('home'))
    return render_template('work_with_codes.html', title='Codes', form=form)

@app.route("/product/new", methods=['GET', 'POST'])
@login_required
def new_product():
    products = Product.query.all()
    form = ProductForm()  
    if form.validate_on_submit():
        product = Product(product_name=form.product_name.data, 
                            product_batch=form.product_batch.data, 
                            expire_date=form.expire_date.data, user_id=current_user.id)
        db.session.add(product)
        db.session.commit()
        flash('Product information was entered to Data Base!', 'success')
        return redirect(url_for('new_code'))
    
    return render_template('work_with_products.html', title='Product data', products=products, form=form)

@app.route("/")
def current_product():
    products = Product.query.all()   
>>>>>>> 05b65c03628311be22d7f5b2fbaf50c2b9c1cb3d
    return render_template('layout.html', products=products)