import os

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app.config.db import db
from app.models.user import User

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            flash("Las contraseñas no coinciden", "error")
            return redirect(url_for("auth.register"))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("El usuario ya existe", "error")
            return redirect(url_for("auth.register"))

        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
        secret_key = os.urandom(24).hex()

        new_user = User(username=username, password=hashed_password, secret_key=secret_key, is_admin=False)
        db.session.add(new_user)
        db.session.commit()

        flash("Registro exitoso, ahora puedes iniciar sesión", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash("Usuario o contraseña incorrectos", "error")
            return redirect(url_for("auth.login"))

        login_user(user)
        flash("Inicio de sesión exitoso", "success")
        return redirect(url_for("home"))

    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada exitosamente", "success")
    return redirect(url_for("auth.login"))