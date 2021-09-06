from flask import Flask
from .models import db
from flask_migrate import Migrate
from flask_moment import Moment


def create_app():
    app = Flask(__name__)
    app.config.from_object('fyyur.config')
    moment = Moment()
    migrate = Migrate()
    moment.init_app(app)
    migrate.init_app(app, db)
    from fyyur.views import pages, errors, forms
    app.register_blueprint(pages.page)
    # app.register_blueprint(errors.error)
    # app.register_blueprint(forms.form)

    return app

if __name__ == '__main__':
    create_app()