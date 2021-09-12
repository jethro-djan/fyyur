from flask import Flask
from .models import db
from flask_migrate import Migrate
from flask_moment import Moment


app = Flask(__name__)
app.config.from_object('fyyur.config')
db.init_app(app)
moment = Moment(app)
moment.init_app(app)
migrate = Migrate(app)
migrate.init_app(app, db)
from fyyur.views import pages, errors, forms
app.register_blueprint(pages.page)
app.register_blueprint(errors.error)
app.register_blueprint(forms.form)


if __name__ == '__main__':
    app.run(debug=True)