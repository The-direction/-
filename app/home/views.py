# coding:utf8
from . import home
from flask import render_template, redirect, url_for, request
from app.models import *

@home.route("/login/", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("home/login.html")
    else:
        user = User()
        contact = request.form.get('contact')
        if contact in User.query.all():
            return redirect(url_for('home.index'))
        return redirect(url_for("home.login"))
@home.route("/logout/")
def logout():
    return redirect(url_for("home.login"))

@home.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("home/register.html")
    else:
        user = User()
        name = request.form.get('name')
        #print(name)
        email = request.form.get('email')
        #print(email)
        phone = request.form.get('phone')
        #print(phone)
        pwd = request.form.get('password')
        #print(pwd)
        repwd = request.form.get('repassword')
        if user.query.filter_by(name=name).first():
            return "名称已存在"
        else:
            user.name = name
            user.email = email
            user.phone = phone
            user.pwd = pwd
            user.repwd = repwd
            db.session.add(user)
            db.session.commit()
            #print(user)
            return "注册成功"
@home.route("/user/")
def user():
    return render_template("home/user.html")

@home.route("/pwd/")
def pwd():
    return render_template("home/pwd.html")

@home.route("/comments/")
def comments():
    return render_template("home/comments.html")

@home.route("/loginlog/")
def loginlog():
    return render_template("home/loginlog.html")

@home.route("/moviecol/")
def moviecol():
    return render_template("home/moviecol.html")

@home.route("/")
def index():
    return render_template("home/index.html")

@home.route("/animation/")
def animation():
    return render_template("home/animation.html")

@home.route("/search/")
def search():
    return render_template("home/search.html")

@home.route("/play/")
def play():
    return render_template("home/play.html")

@home.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"),404











