from flask import Flask
from .models import db
# from fyyur.views import view
from flask_migrate import Migrate
# from flask_moment import Moment

# import fyyur


# moment = Moment()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('fyyur.config')
    # moment.init_app(app)
    migrate.init_app(app, db)
    from fyyur.views import view
    app.register_blueprint(view, url_prefix='/views')

    # import fyyur.views

    return app

if __name__ == '__main__':
    create_app()