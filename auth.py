from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, db

auth = Blueprint('auth', __name__)

# ... Registration, login, and logout routes here ...
