from flask import render_template
from app import create_app, db

from flask_migrate import Migrate

app = create_app('default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return "cmd"

@app.cli.command()
def test():
    
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


with app.app_context():
    db.create_all()


###== Error Handler ==###

@app.errorhandler(403)
def page_not_found(e):
    return render_template('error/forbidden.jinja'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.jinja'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/500.jinja'), 500


if __name__ == "__main__":
    app.run(debug=True)