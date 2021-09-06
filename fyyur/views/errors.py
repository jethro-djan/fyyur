from flask import render_template, Blueprint

error = Blueprint('errors', __name__, template_folder='templates/errors')

@error.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@error.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500