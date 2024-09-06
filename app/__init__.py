import secrets

from flask import Flask, session


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.before_request
    def make_session_permanent():
        session.permanent = True

    app.config['SECRET_KEY'] = secrets.token_urlsafe(30)
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

    from .user_test1.userr import user1
    from .user_test2.user2 import user2 
    from .user_test3.userr import user3
    from .user_test4.userr import user4 

    app.register_blueprint(user1, url_prefix='/user1')
    app.register_blueprint(user2, url_prefix='/t2')
    app.register_blueprint(user3, url_prefix='/t3')
    app.register_blueprint(user4, url_prefix='/t4')

    return app