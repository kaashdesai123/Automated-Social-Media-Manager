from flask import Flask
from .models import db, User
from .auth import auth
from .twitter import twitter_bp
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth)
app.register_blueprint(twitter_bp)

if __name__ == "__main__":
    app.run(debug=True)
