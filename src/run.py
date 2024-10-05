from app import create_app, db
from cli import init_app

app = create_app()
init_app(app)  # adding cli flask support

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()